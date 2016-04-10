# Author: Hessam
# read a video frame, resize it and covert to rgb
import pylab
import imageio
from skimage.transform import resize
from skimage.color import rgb2gray

filename="person15_walking_d1_uncomp.avi"
vid = imageio.get_reader(filename,  'ffmpeg')
#10th frame
frame = vid.get_data(10) 
#resize frame
frame_resized=resize(frame, (100, 100))
#convert the color frame to gray-scale
frame_gray= rgb2gray(frame_resized)

fig = pylab.figure()
fig.suptitle('image #{}'.format(10), fontsize=20)
pylab.imshow(frame_gray)

