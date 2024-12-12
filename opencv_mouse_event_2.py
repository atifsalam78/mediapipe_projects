import numpy as np
import cv2 as cv

# img = np.zeros((512, 512, 3), np.uint8)
img = cv.imread("D:/mediapipe_projects/hand_gesture/data/tomato.jpeg")
cv.imshow("Mouse Event", img)

def click_event(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), 2, (0, 0, 255), -1)
        points.append((x,y))
        # print(points)
        if len(points) >=2:
            cv.line(img, points[-1], points[-2], (0, 0, 255), 1)
        cv.imshow("Mouse Event", img)


points = []
cv.setMouseCallback("Mouse Event", click_event)
cv.waitKey(0)

cv.destroyAllWindows()

