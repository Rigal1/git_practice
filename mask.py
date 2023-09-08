import cv2
import numpy as np

img = cv2.imread("./data/image/kau1.jpg")
img_mask = cv2.imread("./data/image/kau_mask.jpg")
img_mask_hsv = cv2.cvtColor(img_mask, cv2.COLOR_BGR2HSV)

# lower_green = np.array([110 / 360 * 179, 0, 0])
# upper_green = np.array([130 / 360 * 179, 255, 255])
lower_green = np.array([110/360*179, 255, 255])
upper_green = np.array([130/360*179, 255, 255])
green_mask = cv2.inRange(img_mask_hsv, lower_green, upper_green)
print(type(green_mask))
cv2.imwrite("test.jpg", green_mask)