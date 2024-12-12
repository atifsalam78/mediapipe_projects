import numpy as np
import cv2 as cv

img = cv.imread("D:/mediapipe_projects/hand_gesture/data/ronaldo.jpg")

print(img.shape)
print(img.size)
print(img.dtype)
# print(img.device)
# print(img.base)
# print(img.ctypes)
# print(img.data)
# print(img.flags)
# print(img.flat)
# print(img.imag)

b,g,r  = cv.split(img)
# print(b, g, r)
img = cv.merge((b, g, r))

def click_event(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print("x = {}, y = {}".format(x, y))
'''
The co-ordinates used in the array follow the format of 
img [y1: y2, x1: x2]
Therefore, when copying to another part of the image, you need to ensure that (y2-y1) value remains the same, as well as (x2-x1)

Here's another example to copy messi's head, where Top left coordinates is (200, 60) and bottom right is (270, 140) in x,y format

messi_head = img[60:140, 200:270]
img[260:340,100:170] = messi_head
'''
# ball = img[200:225, 266:291]
# img[180:205, 200:225] = ball
# img = ball

ball = img[196:227, 250:300]
img[176:207, 184:234] = ball

cv.imshow("Image", img)
cv.setMouseCallback("Image", click_event)
cv.waitKey(0)
cv.destroyAllWindows()
