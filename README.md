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


-> How to use:
1. Change the host ip appropriately for your use case (in RobStart.py, RobStop.py, and RestAPITestingSignals.py)
host = 'http://127.0.0.1' for a robot on Robot Studio (Your local device); host = 'http://192.168.125.1' if the server computer is connected to the service port of a robot's controller

2. Run RestAPIStart.py

3. Disable the firewall on your server computer

4. Check the IPv4 address of your server computer

5. Remote controlling page should be accessible via IPv4 address:5000 (e.g., 10.131.12.92:5000)

6. If you want to control the robot remotely using a mobile phone or iPad etc., connect its Wifi to the identical one your server computer is connected with.

7. Go to Safari, Chrome, any web browser and type IPv4 address:5000 (e.g., 10.131.12.92:5000)


It was a personal mini project utilizing Flask and Rest API on python.
