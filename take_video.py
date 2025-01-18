""" Take video with any camera """
import cv2
from time import sleep
import os

camera_index = 2
cam = cv2.VideoCapture(camera_index)

while not cam.isOpened():
	cam = cv2.VideoCapture(camera_index)
	print("Waiting for camera...")
	sleep(0.05)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

q_unicode = ord('q')
b_unicode = ord('b')
is_recording = False

while True:
	_, frame = cam.read()

	cv2.imshow('Frame', frame)

	if is_recording:
		out.write(frame)

	key = cv2.waitKey(1)
	if key == b_unicode: # If 'b' is pressed, start recording (Its case sensitive)
		is_recording = not is_recording
		
	if key == q_unicode: # If 'q' is pressed, close program (Its case sensitive)
		break

cam.release()
out.release()
cv2.destroyAllWindows()
