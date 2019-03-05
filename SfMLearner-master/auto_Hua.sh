#!/usr/bin/env tcsh

set gpus=2
set nframes=1440
set nskip=240
set nfold=4# for validation movies

set indirtags=(Trn01 Trn02 Trn03 Trn04 Trn05 Trn06 Trn07  Val01 Val02 Val03 Val04 Val05 Val06 Val07 Val08 Val09)

if (! -d dnn_features_raw) then
  mkdir dnn_features_raw
endif

set n=13

while ($n <= 16)
  set gpuid=`echo "($n-1) % $gpus" | bc`
  set run=`printf %02d $n`

  set imagedir="/home/junjie_hua/brain_SfMLearner/dataset/formatted_data/Nishida_Vimeo_$indirtags[$n]/im*.jpg"

  if ($n < 12) then
    echo ./infer.py "'$imagedir'" $nframes dnn_features_raw/NishidaVimeo_1024x576/NishidaVimeo${run}.zarr --nskip $nskip --gpu $gpuid
    #eval ./infer.py "'$imagedir'" $nframes dnn_features_raw/NishidaVimeo_1024x576/NishidaVimeo${run}.zarr --nskip $nskip --gpu $gpuid
  else 
    echo ./infer.py "'$imagedir'" $nframes dnn_features_raw/NishidaVimeo_1024x576/NishidaVimeo${run}.zarr --nskip $nskip --nfold $nfold --gpu $gpuid
    #eval ./infer.py "'$imagedir'" $nframes dnn_features_raw/NishidaVimeo_1024x576/NishidaVimeo${run}.zarr --nskip $nskip --nfold $nfold --gpu $gpuid
  endif

  @ n = $n + 1

end