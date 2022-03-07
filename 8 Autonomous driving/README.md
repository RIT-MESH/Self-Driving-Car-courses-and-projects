# Autonomous driving

Simulation is used to train a car how to drive and navigate on its own. This simulator is provided to us courtesy of the audacity organization who have set up an open source vehicular simulation built with unity. There are other simulators that can be use for autonomous driving car's simulation like air sim, another self-driving car Open-Source simulator that's based on Unreal Engine.

<p align="center"><img src="https://user-images.githubusercontent.com/74177895/157059734-c5e228fc-9010-498e-ad98-6f1997a5298d.PNG?raw=true"alt="Sublime's custom image"/>
 </p>

# Steps
1) See list of Environment: **conda env list**
2) Conda Environment: **conda create -n drive python=3.7.4** 
3) Activate Environment: **conda activate drive**
4) Install Dependencies: **pip install -r requirement.txt**
5) Run main file: **python drive.py**
6) Deactivate Environment: **conda deactivate**


**->Delete Environment: conda env remove -n nameofevnironment**


Note: if simulator is not connected then use following commands 

1) pip install python-engineio==3.13.2

2) pip install python-socketio==4.6.1

Solution for simulation not connected: [link1](https://github.com/udacity/self-driving-car-sim/issues/131)
                                            or 
                                            [link2](https://github.com/llSourcell/How_to_simulate_a_self_driving_car/issues/34)
