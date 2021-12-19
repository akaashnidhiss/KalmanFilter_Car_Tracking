
import cv2
import numpy as np
from Detect import detect
from Kalman import KalmanFilter

def main():
    # Creating opencv video capture object
    vidCap = cv2.VideoCapture('car5.mp4')

    # Video reading speed
    vrs = 100  
    hspeed = 100

    # Create KalmanFilter object kalmanF
    # KalmanFilter constructor -> KalmanFilter(dt, ux, uy, acceleration, x measurement, y measurement)
    kalmanF = KalmanFilter(0.1, 1, 1, 1, 0.1,0.1)

    while(True):
        # Frame being read
        temp, imageSample = vidCap.read()

        # Detecting a car
        centreArr = detect(imageSample)

        # Centroid tracking if they are being detected by the code:
        if (len(centreArr) > 0):

            # Prediction function
            (x, y) = kalmanF.predict()
            x = int(x)
            y = int(y)

            # Rectangle depicting predicted car position
            cv2.rectangle(imageSample, (x - 15, y - 15), (x + 15, y + 15), (255, 255, 0), 2)

            # Update function
            (x1, y1) = kalmanF.update(centreArr[0])
            x1 = int(x1)
            y1 = int(y1)

            # Rectangle depicting estimated car position
            cv2.rectangle(imageSample, (x1 - 15, y1 - 15), (x1 + 15, y1 + 15), (0, 255, 255), 2)
            center1 = int(centreArr[0][0])
            center2 = int(centreArr[0][1])

            cv2.putText(imageSample, "Estimated Position", (x1 + 15, y1 + 10), 0, 0.5, (0, 255, 255), 2)
            cv2.putText(imageSample, "Predicted Position", (x + 15, y), 0, 0.5, (255, 255, 0), 2)
            cv2.putText(imageSample, "Measured Position", (center1 + 15, center2 - 15), 0, 0.5, (255,0,0), 2)

        cv2.imshow('image', imageSample)

        # To quit program
        if cv2.waitKey(2) & 0xFF == ord('q'):
            vidCap.release()
            cv2.destroyAllWindows()
            break

        cv2.waitKey(hspeed-vrs+1)
        


if __name__ == "__main__":
    main()
