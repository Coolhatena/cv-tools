""" A template script for computer vision projects """
import cv2
from time import sleep

camera_index = 2
cam = cv2.VideoCapture(camera_index)

while not cam.isOpened():
	cam = cv2.VideoCapture(camera_index)
	print("Waiting for camera...")
	sleep(0.05)

q_unicode = ord('q')

while True:
	_, frame = cam.read()

	cv2.imshow('Frame', frame)

	key = cv2.waitKey(1)
	if key == q_unicode: # If 'q' is pressed, close program (Its case sensitive)
		break

cam.release()
cv2.destroyAllWindows()
