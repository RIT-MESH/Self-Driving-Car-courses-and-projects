# Autonomous Robots: Localization

<p align="center"><img src="https://github.com/RIT-MESH/Self-Driving-Car-courses-and-projects/blob/main/4%20Autonomous%20Robots:%20Localization/Autonomous%20Robots%20Localization.jpg?raw=true"alt="Sublime's custom image"/>
</p>


                                course link: https://www.udemy.com/course/autonomous-robots-localization/

# Note:
Package Requirements: python=3.7.4 numpy=1.16.4 matplotlib=3.1.0\
See list of Environment: conda env list\
Conda Environment: conda create -n localization python=3.7.4 numpy=1.16.4 matplotlib=3.1.0\
Activate Environment: conda activate localization\
Deactivate Environment: conda deactivate\
Delete Environment: conda env remove -n nameofevnironment

-----------------------------------------------------------------------------------------------------------
## Assigment 1: Least Squares
-> Based on locations of poles and distance from robot´s position to each of the pole calculate robot´s location.\
-> You don´t know which measuremnet corespond to which pole.\
-> Based on cost function, you will find the location with lowest total cost.\
-> Cost function: (Minimal total distance diference between guess location and pole measurements)**2

### Assigment 2: Bayes rule
-> Bayes rule used to determinate location of robot in 1D world\
-> Bayes rule is used to update probability of some phenomena based on new observation or in other words update your beliefs based on evidence
-> Bayes rule: https://en.wikipedia.org/wiki/Bayes%27_theorem or https://www.youtube.com/watch?v=HZGCoVF3YvM
-> 2-1 -> Robot moves every time exactly same distance with 0 uncertainty
-> 2-2 -> Robots moves with some move uncertainty

### Assigment 3: 1D Particle filter
-> Using Particle filter to determinate location of robot in 1D world\
-> Particle filter used multiple particles (virtual copy of robot) to determinate it position.\
In every loop particles will:
1. Move -> movement of particles is identical to real movement of robot. Only difference is that every particle moves with some uncertainty which is based on gaussian distribution
2. Measure -> Robot and particles scan its environment. Measurement has also some uncertainty
3. Update -> Based on difference between what robot sees and particle sees weights are calculated.
4. Resample -> Some portion of particles with the highest weights will be choosen to be fundamental, and rest of the particles will be resampled around these fundamentals ones.

### Assigment 4: 2D Particle filter
-> Using Particle filter to determinate location of robot in 2D world
