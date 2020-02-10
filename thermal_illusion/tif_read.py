import tifffile as tiff
import numpy as numpy
import cv2

#a = tiff.imread(r'C:\Users\Hayato\Documents\GitHub\personal\thermal_illusion\Lepton_Capture.tif')
#print(a.shape)

im = cv2.imread(r'C:\Users\Hayato\Documents\GitHub\personal\thermal_illusion\Lepton_Capture.tif')
im.dtype