import numpy as np
import cv2 as cv

img = cv.imread("D:/mediapipe_projects/hand_gesture/data/tomato.jpeg")

cv.imshow("Image", img)

def click_event(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv.circle(img, (x, y), 3, (0, 0, 255), -1)
        myColorImage = np.zeros((512, 512, 3), np.uint8)
        myColorImage[:] = [blue, green, red]
        cv.imshow("Color Window",myColorImage)
        
cv.setMouseCallback("Image", click_event)

cv.waitKey(0)
cv.destroyAllWindows()