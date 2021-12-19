import cv2
import numpy as np

# Trained XML classifiers describes some features of the car object we want to detect
car_cascade = cv2.CascadeClassifier( r'CarDetection/cars.xml')

def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    centers = []
    
    # Drawing the border for the car object detected
    if len(cars)>0:
        x, y, w, h = cars[0]
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
        centrex = x + w/2
        centrey = y + h/2
        
        if (w > 20):
            print(w)
            centers.append(np.array([[centrex], [centrey]]))

    return centers