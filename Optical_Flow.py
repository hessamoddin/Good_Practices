import cv2
import numpy as np
from sklearn import preprocessing

filename="mpi_sintel_final_alley_1.avi"

vid = imageio.get_reader(filename,  'ffmpeg')
# number of frames in video
num_frames=vid._meta['nframes']
print(num_frames)

cap = cv2.VideoCapture(filename)

ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
i=0;
for i in xrange(num_frames-1):
    print(i+1)
    ret, frame2 = cap.read()
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    scaler_mag = preprocessing.StandardScaler().fit(mag)
    scaler_ang = preprocessing.StandardScaler().fit(ang)

    tr_mag=scaler_mag.transform(mag)     
    tr_ang=scaler_ang.transform(ang)     
    # now concatenate vectors
    i=i+1
print(num_frames)
cap.release()
cv2.destroyAllWindows()
