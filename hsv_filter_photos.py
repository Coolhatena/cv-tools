""" Test HSV filters on a image file """

import cv2 as cv
import numpy as np

WIN = 'FILTER MARKERS'
image_path = 'img_test1.png'

src = cv.imread(image_path)
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)

cv.namedWindow(WIN)
cv.createTrackbar('MIN_HUE', WIN,   0, 180, lambda _: None)
cv.createTrackbar('MIN_SAT', WIN,   0, 255, lambda _: None)
cv.createTrackbar('MIN_BRI', WIN,   0, 255, lambda _: None)
cv.createTrackbar('MAX_HUE', WIN, 180, 180, lambda _: None)
cv.createTrackbar('MAX_SAT', WIN, 255, 255, lambda _: None)
cv.createTrackbar('MAX_BRI', WIN, 255, 255, lambda _: None)

prev_low = prev_upp = None

while True:
    low = np.array([
        cv.getTrackbarPos('MIN_HUE', WIN),
        cv.getTrackbarPos('MIN_SAT', WIN),
        cv.getTrackbarPos('MIN_BRI', WIN),
    ])
    upp = np.array([
        cv.getTrackbarPos('MAX_HUE', WIN),
        cv.getTrackbarPos('MAX_SAT', WIN),
        cv.getTrackbarPos('MAX_BRI', WIN),
    ])

    if not np.array_equal(low, prev_low) or not np.array_equal(upp, prev_upp):
        msk = cv.inRange(hsv, low, upp)
        filtered = cv.bitwise_and(src, src, mask=msk)
        cv.imshow('FILTER', filtered)
        prev_low, prev_upp = low.copy(), upp.copy()

    if cv.waitKey(1) == ord('b'):
        print('Closing...')
        break

cv.destroyAllWindows()
