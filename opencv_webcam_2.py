import cv2 as cv

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*"XVID")

out = cv.VideoWriter("output.avi", fourcc , 20.0, (640, 480))

print(cap.isOpened())
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # print(f"{cap.get(cv.CAP_PROP_FRAME_WIDTH)} X {cap.get(cv.CAP_PROP_FRAME_HEIGHT)}")
        print("{} X {}".format(cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

        # out.write(frame)
        
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
        cv.imshow("Web Cam Frame", gray)
    
        if cv.waitKey(1) & 0XFF == ord("q"):
            break
    else:
        break
    
cap.release()
out.release()
cv.destroyAllWindows()
