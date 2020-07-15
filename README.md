# ABB_Webservice
ABB robot remote control with REST API Web Service

! This code only works for IRC5 - robotware version 6.x
For robotware 7 and new lines of controllers, the codes should be updated using Robot Web Service API 2.0 as given in https://developercenter.robotstudio.com/webservice


-> Remote controlling
1. For robots on Robot Studio simulation, host is your local device @ host = 'http://127.0.0.1'
2. For robots in real life, the server computer (computer with these codes) should be connected to one of the LAN ports in the robot's controller. Change the host ip to whichever ip the port is assigned with. In the code files(RobStart.py, RobStop.py, and RestAPITestingSignals.py), I have given host = 'http://192.168.125.1' (This works if the LAN cable is connected to the service port of a robot's controller)

-> Functionalities:
1. Robot motion start
2. Robot motion stop
3. Status of each signal (I/O of the robot)
4. Autofill signal search functionality to pinpoint one signal & identify its status from a collection of signals that could go way beyond 100s.


It was a personal mini project utilizing Flask and Rest API on python.
