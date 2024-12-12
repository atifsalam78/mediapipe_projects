import cv2 as cv
import numpy as np

# events = [i for i in dir(cv) if "EVENT" in i]

# print(events)

img = np.zeros((512,512,3), np.uint8)
img  = cv.imread("D:/mediapipe_projects/hand_gesture/data/leopards.jpg")
cv.imshow("Click Mouse Event", img)

def click_event(event, x, y, flags, param):
    
    if event == cv.EVENT_LBUTTONDOWN:
        print("{} , {}".format(x, y))
        
        strXY = "{}, {}".format(x, y)
    
        font = cv.FONT_HERSHEY_COMPLEX_SMALL
        
    
        cv.putText(img, strXY, (x,y), font, 1, (255,255,0), 1, cv.LINE_AA)
    
        cv.imshow("Click Mouse Event", img)
        
    elif event == cv.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x ,y, 1]
        red = img[x ,y, 2]
        
        font = cv.FONT_HERSHEY_COMPLEX_SMALL
        strBGR = "{}, {}, {}".format(blue, green, red)
        
        cv.putText(img, strBGR, (x, y), font, 1, (255, 0, 255), 1, cv.LINE_AA)
        cv.imshow("Click Mouse Event", img)
        
    


cv.setMouseCallback("Click Mouse Event", click_event)

cv.waitKey(0)
cv.destroyAllWindows()