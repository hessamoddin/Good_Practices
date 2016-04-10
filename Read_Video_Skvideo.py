# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 12:34:44 2016

@author: hessam
"""

from skvideo.io import VideoCapture

filename = 'output.avi'

cap = VideoCapture(filename)
cap.open()
cap = VideoCapture(filename)
retval, image_skvideo = cap.read() #first frame
cap.release()
