import math
import cv2

# Get the distance bewteen two points
def calculate_distance(p1, p2):
	return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


# Calculate a middle point between to points
def calculate_middle_point(pt1, pt2):
	x1, y1 = pt1
	x2, y2 = pt2
	x_diff = abs(x1 - x2)
	y_diff = abs(y1 - y2)

	new_x = int(x2 + x_diff/2) if x1 > x2 else int(x1 + x_diff/2)
	new_y = int(y2 + y_diff/2) if y1 > y2 else int(y1 + y_diff/2)

	return (new_x, new_y)


# Transform a value from set A to its equivalent on set B
def linear_scaling(x, minA=-500, maxA=500, minB=0, maxB=255):
	return (x - minA) / (maxA - minA) * (maxB - minB) + minB


# Rotate a line on a image coordinate system (Where the point (0,0) is the top left)
# Returns the corresponding point of the line based on the origin point
# Params:
# originx and originy are are the coordinates of the line origin
# angle is the rotation angle of the line in degrees 
# rad is the lenght of the line, it will define the other coordinate of the line
def rotate_n_deg(originx, originy, angle, rad):
	return (round(originx+rad*math.cos(-math.radians(angle))), round(originy+rad*math.sin(-math.radians(angle))))

# Filter an image based on a given hsv color values range
# Returns a binary imagen with only the values 
# Min: [0, 0, 0]
# Max: [180, 255, 255]
def hsv_color_filter(image, min_hsv, max_hsv):
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	msk = cv2.inRange(hsv, min_hsv, min_hsv)
	filtered = cv2.bitwise_and(image, image, mask= msk)
	filtered_grey = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)
	(thresh, image_bw) = cv2.threshold(filtered_grey, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	
	return image_bw