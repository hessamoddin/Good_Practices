import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('output.avi')
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
imgplot = plt.imshow(frame)
cap.release()
cv2.destroyAllWindows()
print(frame.shape)
