# encoding: utf-8

#  Copyright 2015-present Scikit Flow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

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
#filename="v_shooting_16_03.avi"
#filename=="v_biking_08_01.avi"
#filename="v_biking_06_04.avi"
#filename="v_swing_23_02.avi"
#frame_no=111
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
