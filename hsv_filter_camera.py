""" Test HSV filters on a live camera """

import cv2 as cv
import numpy as np

global LOW, UPP
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

camera_index = 2 # 0
cap = cv.VideoCapture(camera_index)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)	# 640	/	1280	/	1920	/	3840
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)	# 480	/	720 	/	1080	/	2160

if not cap.isOpened():
	print('Camera not found')

while True:
	ret, src = cap.read()
	if not ret:
		break
	
	# src = cv.resize(src, (1920, 1080)) # Rescale frame (for the bigger resolutions)
	cv.imshow('src1', src)

	hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
	msk = cv.inRange(hsv, LOW, UPP)
	filtered = cv.bitwise_and(src,src, mask= msk)
	filtered_grey = cv.cvtColor(filtered, cv.COLOR_BGR2GRAY)
	
	cv.imshow('FILTER', filtered)

	key = cv.waitKey(1)
	if key == (ord('b')):
		print('Exit...')
		break

cv.destroyAllWindows()
