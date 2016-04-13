import pylab
import imageio
from skimage.transform import resize
from skimage.color import rgb2gray
import numpy as np

 
def daisy_extractor(filename,frame_no,new_shape=(120,180)):
#filename="v_shooting_16_03.avi"
#filename=="v_biking_08_01.avi"
#filename="v_biking_06_04.avi"
#filename="v_swing_23_02.avi"
#frame_no=111
    if frame_no<num_frames: 
        frame = vid.get_data(frame_no) 
        frame_resized=resize(frame, new_shape)
        frame_gray= rgb2gray(frame_resized)
        daisy_desc = daisy(frame_gray,step=16, radius=10)
        descs_1D=np.ravel(daisy_desc)
        print(descs_1D.shape)
    else:
        print("Frame number is larger than the length of video")
    return descs_1D
    
vid = imageio.get_reader(filename,  'ffmpeg')
num_frames=vid._meta['nframes']
filename="v_swing_23_02.avi"
frame_no=111
daisy_extractor(filename,frame_no,new_shape=(120,180))
