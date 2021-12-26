# Autonomous Robots: Model Predictive Control

<p align="center"><img src="https://github.com/RIT-MESH/Self-Driving-Car-courses-and-projects/blob/main/Autonomous%20Robots:%20Model%20Predictive%20Control/Autonomous%20Robots%20Model%20Predictive%20Control%20image.jpg?raw=true"alt="Sublime's custom image"/>
</p>

                                  course link: https://www.udemy.com/course/model-predictive-control




# Note:
Package Requirements: python=3.7.4 numpy=1.16.4 matplotlib=3.1.0 scipy=1.2.1\
See list of Environment: conda env list\
Conda Environment: conda create -n MPC python=3.7.4 numpy=1.16.4 matplotlib=3.1.0 scipy=1.2.1\
Activate Environment: conda activate MPC\
Deactivate Environment: conda deactivate\
Delete Environment: conda env remove -n nameofevnironment


### Assigment 0: Intro
-> Intro to MPC shown on temperature regulation\
-> Used to explain cost function and how optimization works

### Assigment 1: Highway speed control
-> More robotic´s related problem, when car cannot exceed speed limit in 1D track

### Assigment 2: Parking Control
-> 2D control problem, where goal is to park car at any selected place\
-> Bicycle model is used to approximately represent model of the car\
-> Cost function is designed so that, sharp turning or accelerating is being punished\
-> Nicely shows how even quite hard task can be easily done with MPC

### Assigment 3: Obstacle Avoidance
-> 2D control problem, where goal is to get to the goal but avoid obstacle at the track\
-> This example demonstrate more complex cost function and what problem can occur when optimization gets stuck in local minimum.\
-> The problem with local minimum will happen only in simulation and if the car and obstacle starts in straight line. (In real life this specific case would not happen due to sensor noise)

