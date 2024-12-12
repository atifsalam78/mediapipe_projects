import numpy as np
import cv2 as cv

img1 = cv.imread("D:/mediapipe_projects/hand_gesture/data/ronaldo_1.jpg")
img2 = cv.imread("D:/mediapipe_projects/hand_gesture/data/messi_1.jpg")
print("Atif Salam")
img1 = cv.resize(img1, (700, 500))
img2 = cv.resize(img2, (700,500))


# dst = cv.add(img1, img2)
dst = cv.addWeighted(img1, 0.65, img2, 0.35, 0)

cv.imshow("Image", dst)
cv.waitKey(0)
cv.destroyAllWindows()
