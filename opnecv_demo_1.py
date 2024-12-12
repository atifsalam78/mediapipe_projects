import cv2 as cv

img = cv.imread("D:/mediapipe_projects/hand_gesture/data/alligator.jpg", -1)

# print(img)

cv.imshow("image_window", img)

k = cv.waitKey(0)

if k == 27:
    cv.destroyAllWindows()
elif k == ord("s"):
    cv.imwrite("D:/mediapipe_projects/hand_gesture/data/alligator_copy.jpg", img)

