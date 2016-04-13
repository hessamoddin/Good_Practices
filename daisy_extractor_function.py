from __future__ import division, print_function, absolute_import
from six.moves import cPickle
import itertools
import os
import sys
import random
import numpy as np
np.random.seed(1337)  # for reproducibility
import imageio
from skimage.transform import resize
from skimage.color import rgb2gray
from skimage.feature import daisy
import Daisy_Extractor

def Daisy_Extractor_Fn(vid,frame_no,new_shape=(120,180),step=16, radius=10):
    if frame_no<num_frames: 
        frame = vid.get_data(frame_no) 
        frame_resized=resize(frame, new_shape)
        frame_gray= rgb2gray(frame_resized)
        daisy_desc = daisy(frame_gray,step=step, radius=radius)
        descs_1D=np.ravel(daisy_desc)
        print(descs_1D.shape)
    else:
        print("Frame number is larger than the length of video")
    return descs_1D
    
filename="/home/hessam/Desktop/practice_code/test_video.avi"
vid = imageio.get_reader(filename,  'ffmpeg')
num_frames=vid._meta['nframes']
frame_no=10
daisy_desc=Daisy_Extractor_Fn(vid,frame_no,new_shape=(120,180))
print(daisy_desc.shape)
