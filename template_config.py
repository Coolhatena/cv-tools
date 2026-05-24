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

camera_index = config.get("camera_index", 0)
# --- fin config ---

IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.webp'}

source = camera_index
if isinstance(source, str):
    ext = os.path.splitext(source)[1].lower()
    source_type = 'image' if ext in IMAGE_EXTS else 'video'
else:
    source_type = 'camera'

if source_type == 'image':
    frame = cv2.imread(source)
    if frame is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {source}")
    cam = None
else:
    cam = cv2.VideoCapture(source)
    if source_type == 'camera':
        while not cam.isOpened():
            cam = cv2.VideoCapture(source)
            print("Waiting for camera...")
            sleep(0.05)
    elif not cam.isOpened():
        raise FileNotFoundError(f"No se pudo abrir el video: {source}")

q_unicode = ord('q')

while True:
	if source_type != 'image':
		ret, frame = cam.read()
		if not ret:
			if source_type == 'camera':
				continue
			else:
				break

	cv2.imshow('Frame', frame)

	key = cv2.waitKey(1)
	if key == q_unicode: # If 'q' is pressed, close program (Its case sensitive)
		break

if cam is not None:
	cam.release()
cv2.destroyAllWindows()
