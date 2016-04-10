import pylab
import imageio

vid = imageio.get_reader(filename,  'ffmpeg')
image = vid.get_data(10) #10th frame
fig = pylab.figure()
fig.suptitle('image #{}'.format(num), fontsize=20)
pylab.imshow(image)
pylab.show()
