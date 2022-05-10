# KalmanFilter_Car_Tracking

### INTRODUCTION
Kalman filtering is an algorithm that allows us to estimate the states of a system given the observations or measurements. It is a useful tool for a variety of different applications including object tracking and autonomous navigation systems, economics prediction, etc.
Even though it is a relatively simple algorithm, it's still not easy for some people to understand and implement it in a computer program such as Python. Therefore, the aim of this tutorial is to help some people to comprehend easily the implementation of Kalman filter in Python.
While there are some excellent references detailing the theory behind the Kalman filter, so we’re not going to dive deeply into the theoretical details. Instead, this article presents the Kalman filter from a practical usage perspective only. 

### BACKGROUND OF STUDY 
Since our purpose of this tutorial is to implement the Kalman filter in computer programing code, we’ll only consider this tutorial for the Discrete Kalman filter.

### LEARNING OUTCOME: 
In the end, it is concluded that we have made effort on the following points: 
- A description of the background and context of the project and its relation to work already done in the area. 
- Made a statement of the aims and objectives of the project. 
- We define the problem on which we are working in the project. 
- We describe the requirement Specifications of the system and the actions that can be done on these things. 
- We understand the problem domain and produce a model of the system, which describes operations that can be performed on the system. 
- We designed the user interface and security issues related to the system. 
- Finally, the system is implemented and tested according to test cases. 

### OUTPUT SCREENSHOTS: 
The following are some output screenshots displayed by our project code, illustrating the Estimated Position, Measured Position and Predicted Position of the car being tracked.
![image](https://user-images.githubusercontent.com/60477228/167597188-0443bdbe-7bb7-44cf-8156-c1b37bb88b1b.png)
![image](https://user-images.githubusercontent.com/60477228/167597259-6aa1d37b-7765-4196-85bc-e1b3d8a6d68a.png)
![image](https://user-images.githubusercontent.com/60477228/167597315-efa576b2-db8f-407a-b4d5-351cf66a4fa7.png)
![image](https://user-images.githubusercontent.com/60477228/167597348-abf91011-8b9e-45d5-b8d7-6549f0f7ac37.png)
![image](https://user-images.githubusercontent.com/60477228/167597407-e8507c49-0fd3-4b1c-8b20-afb4a80fb803.png)
![image](https://user-images.githubusercontent.com/60477228/167597445-2294d71d-5731-48d1-aa5e-dda698812918.png)

A video featuring a sample output of our project code can be found here in the following google drive link:
!carOutput.avi[https://drive.google.com/file/d/1W9r0hor1ZZUcZeaO5FhJ9IyRSe92XLgf/view?usp=sharing]

### CONCLUSION: 
In conclusion, Kalman filtering is an algorithm that allows us to estimate the states of a system given the observations or measurements. It is a useful tool for a variety of different applications including object tracking and autonomous navigation systems, economics prediction, etc.
We implement the same in python, with the project having three files, namely: Kalman.py, Detect.py, and main.py.
Kalman.py contains one class called KalmanFilter consisting of three functions, __init__(), predict(), and update().
Detect.py file plays a role as an object detector and main.py is the main file of this project that we’ll execute to track an object. At the beginning of this file, we import the function detect() from the file Detector.py, and class KalmanFilter from the file Kalman.py.

### FUTURE ASPECTS: 
In order to create an algorithm which reacted quickly to changes (Process Noise) in the object being detected, the Kalman Gain coefficient was accordingly increased in order to properly and quickly react to these changes. However, during the work on this project, it was realised that the car detector algo (contained in Detect.py) identified non-car objects and mistyped them as cars. Thus, the performance of the algorithm suffers when faced with high levels of measurement noise. 
In order to enhance the working of the project code, necessary modifications should be performed to enhance the car detection algorithm and thus decrease overall measurement noise.

### LITERATURE REVIEW:
The following papers were looked into to understand the Kalman Filter:
- Welch, G., & Bishop, G. (1995). An introduction to the Kalman filter.
- Meinhold, Richard J. & Singpurwalla, Nozer D. (1983). Understanding the Kalman Filter. The American Statistician, 37(2), 123–127.
- Cox, Ingemar J. & Wilfong, Gordon T. (1990). Autonomous Robot Vehicles || The Kalman Filter: An Introduction to Concepts. , 10.1007/978-1-4613-8997-2(Chapter 15), 194–204.
- Fitzgerald, R. (1971). Divergence of the Kalman filter. IEEE Transactions on Automatic Control, 16(6), 736–747.
- Thacker, N. A., & Lacey, A. (1998). Tutorial: The kalman filter. Imaging Science and Biomedical Engineering Division, Medical School, University of Manchester, 61.
Yi, D. (1977). Kalman filter.
- Rojas, R. (2003). The kalman filter. available on www. robocup. mi. fu-berlin. de/buch/kalman. pdf, 1-7.
- Faragher, Ramsey (2012). Understanding the Basis of the Kalman Filter Via a Simple and Intuitive Derivation [Lecture Notes]. IEEE Signal Processing Magazine, 29(5), 128–132.
- Humpherys, Jeffrey; Redd, Preston; West, Jeremy  (2012). A Fresh Look at the Kalman Filter. SIAM Review, 54(4), 801–823.
- Chan, Y.t.; Hu, A.g.c.; Plant, J.B.  (1979). A Kalman Filter Based Tracking Scheme with Input Estimation. IEEE Transactions on Aerospace and Electronic Systems, AES-15(2), 237–244.

To improve the algorithm of the Kalman Filter used in the project, the following research papers were referred to:
- Robustifying the Kalman Filter by developing a model where posterior distribution reverts to the prior distribution when extreme outlying observations are encountered.
- Meinhold, Richard J.; Singpurwalla, Nozer D.  (1989). Robustification of Kalman Filter Models. Journal of the American Statistical Association, 84(406), 479–486.
- Robust Bayesian Estimation for the Linear Model and Robustifying the Kalman Filter.
- Masreliez, C.; Martin, R.  (1977). Robust bayesian estimation for the linear model and robustifying the Kalman filter. IEEE Transactions on Automatic Control, 22(3), 361–371.
- Analysis and Improvement of the Consistency of Extended Kalman Filter based SLAM
- Huang, Guoquan P.; Mourikis, Anastasios I.; Roumeliotis, Stergios I.  (2008).  [IEEE 2008 IEEE International Conference on Robotics and Automation (ICRA) - Pasadena, CA, USA (2008.05.19-2008.05.23)] 2008 IEEE International Conference on Robotics and Automation - Analysis and improvement of the consistency of extended Kalman filter based SLAM. , (), 473–479.  
- Improvement of Observer/Kalman Filter Identification (OKID) by Residual Whitening.
- Phan, M.; Horta, L. G.; Juang, J.-N.; Longman, R. W.  (1995). Improvement of Observer/Kalman Filter Identification (OKID) by Residual Whitening. Journal of Vibration and Acoustics, 117(2), 232–.   
