import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv.imshow("Web Cam Frame", frame)
    
    if cv.waitKey(1) & 0XFF == ord("q"):
        break
    
cap.release()
cv.destroyAllWindows()