import numpy as np
import cv2 as cv

img1 = cv.imread("D:/mediapipe_projects/hand_gesture/data/tiger.jpeg")
img1 = cv.resize(img1, (500,500))

img2 = np.zeros((500, 500, 3), np.uint8)
img2 = cv.rectangle(img2, (200,0), (300,100), (255, 255, 255), -1)

# bitAnd = cv.bitwise_and(img2, img1)
# bitOr = cv.bitwise_or(img2, img1)
# bitXor = cv.bitwise_xor(img2, img1)
bitNot1 = cv.bitwise_not(img1)
bitNot2 = cv.bitwise_not(img1)


cv.imshow("Image1", img1)
cv.imshow("Image2", img1)
# cv.imshow("Bit And", bitAnd)
# cv.imshow("Bit Or", bitOr)
# cv.imshow("Bit XOR", bitXor)
cv.imshow("Bit Not 1", bitNot1)
cv.imshow("Bit Not 2", bitNot2)

cv.waitKey(0)
cv.destroyAllWindows()
