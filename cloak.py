import cv2
import numpy as np
import time

# Start camera
cap = cv2.VideoCapture(0)
time.sleep(0)  # wait for camera to adjust

background = 0

# Capture the background (60 frames for stability)
for i in range(60):
    ret, background = cap.read()
background = np.flip(background, axis=1)  # mirror image

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break
    
    img = np.flip(img, axis=1)
    
    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Red color range ( tweak these values)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    

    mask = mask1 + mask2

    # Refine mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations=1)

    # Separate cloak and rest of image
    cloak_area = cv2.bitwise_and(background, background, mask=mask)
    rest_area = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))
    
    final_output = cv2.addWeighted(cloak_area, 1, rest_area, 1, 0)

    cv2.imshow("Cloak", final_output)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
