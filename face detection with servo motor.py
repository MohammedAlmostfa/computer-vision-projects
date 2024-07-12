#This project controls the angle of rotation of a servo motor by analyzing the location of the recognized face

import dlib
import cv2
import pyfirmata2
from time import sleep

def convert_to_new_range(number):
    
    new_value = (number / 500) * 180
    return new_value

board = pyfirmata2.Arduino("com8")
pin9 = board.get_pin('d:9:s')
sleep(0.015)


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    for face in faces:
        x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
        
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1) 

        
    
        landmarks = predictor(gray, face)  
        for n in range(0, 68):
            x, y = landmarks.part(n).x, landmarks.part(n).y
            if center_x >300:
              cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
            else:
              cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)
        new_values =convert_to_new_range(center_x)
        #print(new_values)
        pin9.write(new_values)  




        cv2.imshow("frame",frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
