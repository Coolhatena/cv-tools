""" A template script for computer vision projects, ready to be used with a config.json file """
import cv2
import json
import os
from time import sleep

# --- config ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

config = {}
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)

camera_index = int(config.get("camera_index", 0))
# --- fin config ---
cam = cv2.VideoCapture(camera_index)

# Double check for slow cameras
while not cam.isOpened():
	cam = cv2.VideoCapture(camera_index)
	print("Waiting for camera...")
	sleep(0.05) # Micro-tic between tries

q_unicode = ord('q')

while True:
	_, frame = cam.read()

	cv2.imshow('Frame', frame)

	key = cv2.waitKey(1)
	if key == q_unicode: # If 'q' is pressed, close program (Its case sensitive)
		break

cam.release()
cv2.destroyAllWindows()
