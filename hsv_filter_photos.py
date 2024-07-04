""" Test HSV filters on a image file """

import cv2 as cv
import numpy as np

global LOW, UPP

image_path = 'img_test1.png'

LOW = np.array([0,0,0])
UPP = np.array([180,255,255])


cv.namedWindow('FILTER MARKERS')

def min_hue(MINHUE):
	LOW[0] = MINHUE

def min_sat(MINSAT):
	LOW[1] = MINSAT

def min_bri(MINBRI):
	LOW[2] = MINBRI

def max_hue(MAXHUE):
	UPP[0] = MAXHUE

def max_sat(MAXSAT):
	UPP[1] = MAXSAT

def max_bri(MAXBRI):
	UPP[2] = MAXBRI


cv.createTrackbar('MIN_HUE', 'FILTER MARKERS' , 0, 180, min_hue)
cv.createTrackbar('MIN_SAT', 'FILTER MARKERS' , 0, 255, min_sat)
cv.createTrackbar('MIN_BRI', 'FILTER MARKERS' , 0, 255, min_bri)

cv.createTrackbar('MAX_HUE', 'FILTER MARKERS' , 180, 180, max_hue)
cv.createTrackbar('MAX_SAT', 'FILTER MARKERS' , 255, 255, max_sat)
cv.createTrackbar('MAX_BRI', 'FILTER MARKERS' , 255, 255, max_bri)

while True:
    src = cv.imread(image_path)
    cv.imshow('FILTER',src)

    hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)

    msk = cv.inRange(hsv, LOW, UPP)
    filtered = cv.bitwise_and(src,src, mask= msk)
    cv.imshow('FILTER', filtered)

    key = cv.waitKey(1)
    if key == (ord('b')):
        print('Exit...')
        break


cv.waitKey(0)
cv.destroyAllWindows()
