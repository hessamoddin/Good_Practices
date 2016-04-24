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
from __future__ import print_function
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
from keras.preprocessing import sequence
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from keras.datasets import imdb
import matplotlib.cbook as cbook

############################## Functions  ########################################
def Split_Sequence(video_features,num_frames,timesteps):
       return 0
        
def Daisy_Extractor_Fn(vid,frame_no,new_shape=(120,180),step=50, radius=20):
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
    else:
        print("Frame number is larger than the length of video")
    return descs_1D
    
############################## Parameters  ########################################
timesteps=20
batch_size = 32

filename="/home/hessam/Desktop/practice_code/v_biking_06_04.avi"
vid = imageio.get_reader(filename,  'ffmpeg')
num_frames=vid._meta['nframes']
video_features=[]

# Extract and concatenate Daisy features
for frame_no in xrange(num_frames):    
     daisy_desc=Daisy_Extractor_Fn(vid,frame_no)
     video_features.append(daisy_desc)
video_features = np.array(video_features)
data_dim=daisy_desc.shape[0]

print('Feature dimention: %d'%data_dim)
print('Num of frames: %d'%num_frames)




