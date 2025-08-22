import cv2
from time import sleep

camera_indexes = [0, 2]

cams = [cv2.VideoCapture(idx) for idx in camera_indexes]

for i, cam in enumerate(cams):
	while not cam.isOpened():
		cams[i] = cv2.VideoCapture(camera_indexes[i])
		print(f"Waiting for camera {camera_indexes[i]}...")
		sleep(0.05)

frame_sizes = [
	(int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)))
	for cam in cams
]

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
outs = [
	cv2.VideoWriter(f"out{i+1}.mp4", fourcc, 20.0, frame_sizes[i])
	for i in range(len(cams))
]

# Control keys
q_unicode = ord('q')
b_unicode = ord('b')
is_recording = False


while True:
	frames = []
	for cam in cams:
		ret, frame = cam.read()
		if not ret:
			frame = None
		frames.append(frame)

	for i, frame in enumerate(frames):
		if frame is not None:
			cv2.imshow(f'Camera {camera_indexes[i]}', frame)
			if is_recording:
				outs[i].write(frame)

	key = cv2.waitKey(1)
	if key == b_unicode:
		is_recording = not is_recording
		print("Recording:", is_recording)

	if key == q_unicode:
		break

# Free all locked data and close windows
for cam in cams:
	cam.release()
for out in outs:
	out.release()
cv2.destroyAllWindows()
