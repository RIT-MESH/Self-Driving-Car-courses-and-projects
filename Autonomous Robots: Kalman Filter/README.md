## Autonomous Robots: Kalman Filter

Course Link: www.udemy.com/course/autonomous-robots-kalman-filter/
<p align="center"><img src="https://github.com/RIT-MESH/Self-Driving-Car-courses-and-projects/blob/main/Autonomous%20Robots:%20Kalman%20Filter/147134154-8d6bd58f-bfd8-481b-9906-7d43bd586ddd.png?raw=true"alt="Sublime's custom image"/>
</p>



### Autonomous Robots Are The Future. Learn to Program Them With this Fast, Easy to Understand Course!

Assignment 1: Toy Implementation
-> Intro to localization and principle of Kalman filter using simple model of car in 1D spacer
-> Used to explain prediction of speed based on collected data and new measurement. i.e. The speed cannot change abruptly

Assignment 2: 1D Kalman Filter
-> Same problem as in assignment 1, but this time Linear Kalman filter is used to localize car
-> Explains how to setup Kalman filter and what individual matrices are used for

Assignment 3: 2D Kalman Filter
-> Goal is to localize car as precise as possible while driving on a street with turns and traffic lights
-> Program will not only recieve measurement but also vector U (user input)

Assignment 4: Traffic light prediction
-> In this assignment car is approaching intersection and at some point traffic light will change to red
-> Car need to decide if it will make to other side. And based on this prediction needs to decide to stop or continue
-> In first scenario car makes prediction based on current state
-> In second scenario car makes prediction based on current state but also on fact that it is allowed to raise speed for 1 sec

# Note:
Package Requirements: python=3.7.4 numpy=1.16.4 matploblib=3.1.0\
See list of Environment: conda env list\
Conda Environment: conda create -n Kalman python=3.7.4 numpy=1.16.4 matplotlib=3.1.0\
Activate Environment: conda activate Kalman\
Deactivate Environment: conda deactivate\
Delete Environment: conda env remove -n nameofevnironment
