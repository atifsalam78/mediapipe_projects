import numpy as np
import cv2 as cv

img = cv.imread("D:/mediapipe_projects/hand_gesture/data/cat.jpg")

# img = np.zeros([512, 512, 3], np.uint8)

imge = cv.line(img, (0,0), (255,255), (0,0,255), 10)
img = cv.arrowedLine(imge, (0,255), (255,255), (255, 0, 0), 5)

img = cv.rectangle(img, (100,100), (500,500), (0,255,0), 6)

img = cv.circle(img, (200,200), 63, (0,255,0), 10)

font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX

img = cv.putText(img, "This is opencv geometry demonstration", (10, 600), font, 1.5, (0, 0, 255), 3, cv.LINE_AA)

cv.imshow("Geometry", img)

cv.waitKey(0)


cv.destroyAllWindows()



 