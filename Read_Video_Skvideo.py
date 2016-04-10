import skvideo.io
import skvideo.datasets
videogen = skvideo.io.vreader(skvideo.datasets.bigbuckbunny())
for frame in videogen:
        print(frame.shape)
