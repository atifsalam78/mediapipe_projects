import cv2 as cv
import datetime as dt

cap = cv.VideoCapture(0)

WIDTH = cap.get(cv.CAP_PROP_FRAME_WIDTH)
HEIGHT = cap.get(cv.CAP_PROP_FRAME_HEIGHT)


# print("{} X {}".format(WIDTH, HEIGHT))


# cap.set(3, 1280)
# cap.set(4, 720)

# NEW_WIDTH = cap.get(3)
# NEW_HEIGHT = cap.get(4)

# print("{} X {}".format(NEW_WIDTH, NEW_HEIGHT))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # cv.imshow("Grey Frame", grey)
        
        font = cv.FONT_HERSHEY_COMPLEX_SMALL
        text = "Width: {}, Height: {}".format(WIDTH, HEIGHT)
        date_text = str(dt.datetime.now())
        cv.putText(frame, text, (10, 30), font, 1, (0,0,255), 1, cv.LINE_AA)
        cv.putText(frame, date_text, (10, 50), font, 1, (0,0,255), 1, cv.LINE_AA)
        
        cv.imshow("frame", frame)
        
        if cv.waitKey(1) & 0XFF == ord("q"):
            break        
    else:
        break
    
cap.release()
cv.destroyAllWindows()
