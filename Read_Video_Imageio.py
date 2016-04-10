import pylab
import imageio
from skimage.transform import resize
from skimage.color import rgb2gray

filename="/home/hessam/Desktop/movies/Downton Abbey _ Starts Sunday 20 September-WPwaCjE8DcY.mkv"
vid = imageio.get_reader(filename,  'ffmpeg')
# number of frames in video
num_frames=vid._meta['nframes']
#10th frame
frame = vid.get_data(1) 
#resize frame
frame_resized=resize(frame, (100, 100))
#convert the color frame to gray-scale
frame_gray= rgb2gray(frame_resized)

fig = pylab.figure()
fig.suptitle('image #{}'.format(10), fontsize=20)
pylab.imshow(frame_gray)
