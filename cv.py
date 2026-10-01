import cv2
import numpy as np
cap =cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error:Could not Open camera.")
    exit()

while True:
    ret,frame=cap.read()
    if not ret:
        print("Failed to capture frame")
        break 

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red=np.array([0,50,50])
    upper_red=np.array([10,255,255])

    mask=cv2.inRange(hsv, lower_red, upper_red)

    result=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Camera",result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
