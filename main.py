import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # mask 1 

    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    # mask 2
     
    # lower_bound1 = np.array([0, 195, 50])
    # upper_bound1 = np.array([10, 255, 255])

    # lower_bound2 = np.array([169, 195, 50])
    # upper_bound2 = np.array([180, 255, 255])

    # mask1 = cv2.inRange(hsv_frame, lower_bound1, upper_bound1)
    # mask2 = cv2.inRange(hsv_frame, lower_bound2, upper_bound2)
    # mask = mask2+mask1
    # red = cv2.bitwise_and(frame, frame, mask=mask)
    

    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)

    # cv2.waitKey(0)
    # cap.release()
    # cv2.destroyAllWindows()
   
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break