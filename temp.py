import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)

    mask = cv2.inRange(hsv, low_red, high_red)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()