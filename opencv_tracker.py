import numpy as np
import cv2 as cv

def nothing(x):
    print(x)
    
# img = cv.imread("D:/mediapipe_projects/hand_gesture/data/messi_1.jpg")
img = np.zeros((300, 500, 3), np.uint8)

cv.namedWindow("Tracker")

cv.createTrackbar("B", "Tracker", 0, 255, nothing)
cv.createTrackbar("G", "Tracker", 0, 255, nothing)
cv.createTrackbar("R", "Tracker", 0, 255, nothing)
switch = "0: OFF\n 1: ON"
cv.createTrackbar(switch, "Tracker", 0, 1, nothing)

while (1):
    cv.imshow("Tracker", img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    b = cv.getTrackbarPos("B", "Tracker")
    g = cv.getTrackbarPos("G", "Tracker")
    r = cv.getTrackbarPos("R", "Tracker")
    s = cv.getTrackbarPos(switch, "Tracker")
    
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()