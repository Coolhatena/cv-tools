""" Generate polygon mask for post-procesing """

import numpy as np
import cv2

image_path = './img_test.png'

img = cv2.imread(image_path)
mark_img = img.copy()

global pts
pts = []

def click_event(event, x, y, flags, params): 
    global pts
    # checking for left mouse clicks 
    if event == cv2.EVENT_LBUTTONDOWN: 
        pts.append([x, y])

cv2.namedWindow('image')
cv2.setMouseCallback('image', click_event)

while True:
    for pt in pts:
        cv2.circle(mark_img, pt, 5, (0, 0, 255))
        
    cv2.imshow("image", mark_img)
    
    key = cv2.waitKey(1)
    
    if key == ord('b'):
        ## (1) Crop the bounding rect
        pts = np.array(pts)
        rect = cv2.boundingRect(pts)
        x,y,w,h = rect
        cropped = img.copy()
        
        mask = np.zeros(cropped.shape[:2], np.uint8)
        cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)
        dst = cv2.bitwise_and(cropped, cropped, mask=mask)
        bg = np.ones_like(cropped, np.uint8)*255
        cv2.bitwise_not(bg,bg, mask=mask)
        dst2 = bg+ dst        
        cv2.imshow("croped", cropped)
        cv2.imshow("mask", mask)
        cv2.imshow("dst", dst)
        cv2.imshow("dst2", dst2)
        cv2.imwrite("mask_img.png", mask)


    if key == ord('q'):
        break




