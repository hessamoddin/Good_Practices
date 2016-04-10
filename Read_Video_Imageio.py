import pylab
import imageio
filename="test_video.avi"
vid = imageio.get_reader(filename,  'ffmpeg')
frame = vid.get_data(10) #10th frame
fig = pylab.figure()
fig.suptitle('image #{}'.format(num), fontsize=20)
pylab.imshow(frame)
pylab.show()
