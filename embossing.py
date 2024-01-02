import cv2
import numpy as np


img = cv2.imread("test\\002.jpg")
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mask1 = np.array([[-1,0,0],[0,0,0],[0,0,1]])
mask2 = np.array([[1,1,1],[1,-8,1],[1,1,1]])

out1 = cv2.filter2D(gray,-1,mask1)
out2 = cv2.filter2D(gray,-1,mask2)

cv2.imshow("original", gray)
cv2.imshow('mask1', out1)
cv2.imshow('mask2', out2)

cv2.waitKey(0)