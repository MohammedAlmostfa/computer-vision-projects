import cv2
import pyfirmata2
from time import sleep

board = pyfirmata2.Arduino("com8")
pin9 = board.get_pin('d:9:s')
sleep(0.015)

cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    # Pick pixel value
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    color = "Undefined"
    if hue_value < 5:
        color = "RED"
        pin9.write(0)  # دورة إلى اليمين (0 درجة)
        sleep(1)  
    elif hue_value < 22:
        color = "ORANGE"
        pin9.write(180)  # دورة إلى اليمين (0 درجة)
        sleep(1)  
    elif hue_value < 33:
        color = "YELLOW"
        pin9.write(0)  # دورة إلى اليمين (0 درجة)
        sleep(1)  
    elif hue_value < 78:
        color = "GREEN"
        pin9.write(180)  # دورة إلى اليمين (0 درجة)
        sleep(1) 
    elif hue_value < 131:
        color = "BLUE"
        pin9.write(0)  # دورة إلى اليمين (0 درجة)
        sleep(1) 
    elif hue_value < 170:
        color = "VIOLET"
        pin9.write(180)  # دورة إلى اليمين (0 درجة)
        sleep(1) 
    else:
        color = "RED"

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    cv2.imshow("Frame", frame)
    #out.write(frame) #save your video
    key = cv2.waitKey(1)
    if key == "q":
        break

cap.release()

cv2.destroyAllWindows()