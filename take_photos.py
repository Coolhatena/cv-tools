""" Take photos with any camera """
import cv2
from time import sleep
import os

camera_index = 0
cam = cv2.VideoCapture(camera_index)

while not cam.isOpened():
	cam = cv2.VideoCapture(camera_index)
	print("Waiting for camera...")
	sleep(0.05)

img_folder = 'images/'
q_unicode = ord('q')
b_unicode = ord('b')
counter = 0

while True:
	_, frame = cam.read()

	cv2.imshow('Frame', frame)

	key = cv2.waitKey(1)
	if key == b_unicode:
		cv2.imwrite(os.path.join(img_folder, f'img{counter}.png')  , frame) # Save images on img folder
		counter += 1
		print(f'Image no. {counter} saved.')

	if key == q_unicode: # If 'q' is pressed, close program (Its case sensitive)
		break

cam.release()
cv2.destroyAllWindows()
