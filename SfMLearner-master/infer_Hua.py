
import os
import sys
import glob
import numpy as np
import argparse
import io
from PIL import Image
import h5py
import zarr

parser = argparse.ArgumentParser()
parser.add_argument('inimages', help='input images in glob string')
parser.add_argument('nframe', help='number of frames to process per inference', default=24, type=int
)
parser.add_argument('outfile', help='output file (.zarr)')
parser.add_argument('--nskip', help='number of images at the beginning to skip', default=0, type=int
)
parser.add_argument('--nfold', help='number of repetition in the image sequence', default=1, type=in
t)
parser.add_argument('--gpu',  help='gpu id to use (0, 1, ...)', default="0")
parser.add_argument('--verbose',  help='whether to output all caffe logging', action='store_true')

# Check arguments
args = parser.parse_args()

# imagedir
img_files = glob.glob(args.inimages)
if(not img_files):
    raise BaseException('inimages not exist: '+args.inimages)
img_files.sort()
n_image = len(img_files)
print("Number of input images: {}".format(n_image))
n_skip = args.nskip
if (n_skip > 0):
    if (n_skip >= n_image):
        raise BaseException('number specified for --nskip ({}) exceeds the total number of images'.format(n_skip))
    else:
        raise BaseException('number specified for --nskip ({}) exceeds the total number of images'.format(n_skip))
    else:
        print("Skipping first {} images".format(n_skip))
n_total = n_image - n_skip
n_fold = args.nfold
if (n_fold > 1):
    n_total = n_total / n_fold
    n_image = n_skip + n_total
    print("Processing only the first of {} repetitions".format(n_fold))

print("Number of images to process: {}".format(n_total))
    
# outfile
zarr_fp = args.outfile
_, ext = os.path.splitext(zarr_fp)
if not ext == '.zarr':
    raise BaseException('Outfile not in .zarr format\n{}'.format(zarr_fp))

if os.path.exists(zarr_fp):
    raise BaseException('outdir already exsit\n{}'.format(zarr_fp))

outdir, outbase = os.path.split(os.path.abspath(args.outfile))
if not os.path.exists(outdir):
    os.makedirs(outdir)

# gpu
os.environ['CUDA_VISIBLE_DEVICES'] = args.gpu

# Run inference
import torch
torch.set_default_tensor_type('torch.cuda.FloatTensor')
from torch.autograd import Variable
from mymodel import MyModel

mymodel = MyModel()
preprocess = mymodel.preprocess()
labels = mymodel.labels()

store = zarr.DirectoryStore(zarr_fp)
root = zarr.group(store=store, overwrite=True)

for ibeg in np.arange(n_skip, n_image, args.nframe):
    iend = np.min((ibeg + args.nframe, n_image))
    _, f_beg = os.path.split(img_files[ibeg])
    _, f_end = os.path.split(img_files[iend-1])
    print("Images {}-{}: ".format(f_beg, f_end), end='')

    print("preproc...", end='')
    sys.stdout.flush()
    imgs = []
    for jj in range(ibeg, iend):
        img = preprocess(Image.open(img_files[jj])).cuda()
        if img.shape[0] == 1:
            img = img.repeat(3, 1, 1)
        imgs.append(img[None, :, :, :])
    imgs = torch.cat(imgs)
#    print("DEBUG: imgs.shape={}".format(imgs.shape))
    print("ok, ", end='')

    print("infer...", end='')
    sys.stdout.flush()
    output = mymodel.forward(Variable(imgs))
    print("ok, ", end='')

    print("save...", end='')
    sys.stdout.flush()
    for iLayer, layer_name in enumerate(labels):
        n_sample = output[iLayer].shape[0]
        n_feature = np.prod(output[iLayer].shape[1:])
#        print("DEBUG: (n_sample,n_feature)=({},{})".format(n_sample, n_feature))
        if ibeg == n_skip:
            root.create_dataset(layer_name, shape=(n_total, n_feature), chunks=(args.nframe, None), dtype=np.float32)
#        print("DEBUG: index = ({},{})".format(ibeg-n_skip,iend-n_skip))
        root[layer_name][(ibeg-n_skip):(iend-n_skip), :] = torch.reshape(output[iLayer].detach(), (n_sample, n_feature))
    print('ok')
    sys.stdout.flush()