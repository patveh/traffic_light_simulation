# traffic-light-simulation

This project implements:

    - An implementation of a traffic light simulator,
    - An API to an imaginary traffic light device (the simulator),
    - A Robot Framework task which is used to change the operational mode of the simulator.


# Required installations

    - Robot Famework: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#installation-instructions
    - python 3: https://www.python.org/downloads/
    - Flask: https://pypi.org/project/Flask/

# Demo instructions

Open a terminal:

    - clone this project
    - navigate to the project folder /traffic-light-simulation/traffic_light_simulator
        - set environment variables and start Flask
            - windows machine:
                > set FLASK_APP=traffic_light_api.py
                > set FLASH_DEBUG=True
                > flask run
            - linux and mac machines:
                > export FLASK_APP=traffic_light_api.py
                > export FLASH_DEBUG=True
                > flask run

Open a browser:

    - enter the traffic light simulator URL: http://localhost:5000/trafficlight:
    - the traffic light simuator should bink on the yellow light

Open a second terminal:

    - navigate to the project folder /traffic-light-simulation and run the simulation:
        > robot demo_traffic_light_sequence.robot
        - follow the simulation on the traffic light simualtor browser page
        - check the terminal windows for status of the simulation run
