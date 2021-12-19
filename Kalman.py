import numpy as np
import matplotlib.pyplot as plt

class KalmanFilter(object):
    def __init__(self, dt, ux,uy, std_acc, x_measuredSD, y_measuredSD):
        """
       dt -> sampling time (time for 1 cycle)
       ux -> acceleration in x-direction
       uy -> acceleration in y-direction
       std_acc -> process noise magnitude
       x_measuredSD -> standard deviation of the measurement in x-direction
       y_measuredSD -> standard deviation of the measurement in y-direction

       """
        # Sampling time
        self.dt = dt

        # The control input variables
        self.u = np.matrix([[ux],[uy]])

        # Intial State
        self.x = np.matrix([[0], [0], [0], [0]])

        # State Transition Matrix A
        self.A = np.matrix([[1, 0, self.dt, 0],
                            [0, 1, 0, self.dt],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])

        # Control Input Matrix B
        self.B = np.matrix([[(self.dt**2)/2, 0],
                            [0,(self.dt**2)/2],
                            [self.dt,0],
                            [0,self.dt]])

        # Measurement Mapping Matrix
        self.H = np.matrix([[1, 0, 0, 0],
                            [0, 1, 0, 0]])

        #Initial Process Noise Covariance
        self.Q = np.matrix([[(self.dt**4)/4, 0, (self.dt**3)/2, 0],
                            [0, (self.dt**4)/4, 0, (self.dt**3)/2],
                            [(self.dt**3)/2, 0, self.dt**2, 0],
                            [0, (self.dt**3)/2, 0, self.dt**2]]) * std_acc**2

        #Initial Measurement Noise Covariance
        self.R = np.matrix([[x_measuredSD**2,0],
                           [0, y_measuredSD**2]])

        #Initial Covariance Matrix
        self.P = np.eye(self.A.shape[1])

    def predict(self):
        # Update time state
        #x_k =Ax_(k-1) + Bu_(k-1)     
        self.x = np.dot(self.A, self.x) + np.dot(self.B, self.u)

        # Calculate error covariance
        # P= A*P*A' + Q               
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q
        return self.x[0:2]

    def update(self, z):
        # S = H*P*H'+R
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R

        # Kalman Gain Calculation
        # K = P * H'* inv(H*P*H'+R)
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))  

        self.x = np.round(self.x + np.dot(K, (z - np.dot(self.H, self.x))))   

        I = np.eye(self.H.shape[1])

        # Update error covariance matrix
        self.P = (I - (K * self.H)) * self.P   
        return self.x[0:2]
