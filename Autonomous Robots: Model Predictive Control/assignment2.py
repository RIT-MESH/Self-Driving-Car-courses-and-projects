import numpy as np
from sim.sim2d import sim_run

# Simulator options.
options = {}
options['FIG_SIZE'] = [8,8]
options['OBSTACLES'] = False

class ModelPredictiveControl:
    def __init__(self):
        self.horizon = 2
        self.dt = 0.2
        self.L = 2.5  # Car base [m]
        # Reference or set point the controller will achieve.
        self.reference1 = [10, 10, 0]
        self.reference2 = None #[10, 2, 3.14/2]

    def plant_model(self,prev_state, dt, pedal, steering):
        x_t = prev_state[0]
        y_t = prev_state[1]
        psi_t = prev_state[2]
        v_t = prev_state[3]

        return [x_t, y_t, psi_t, v_t]

    def cost_function(self, u, *args):
            state = args[0]
            ref = args[1]
            cost = 0.0

            for k in range(0,self.horizon):
                ts = [0,1]
                v_start = state[3]
                state = self.plant_model(state, self.dt, u[k*2], u[k*2+1])
                # position cost
                cost += abs(ref[0] - state[0])**2
                cost += abs(ref[1] - state[1])**2
                #angle cost
                cost += abs(ref[2] - state[2])**2
                #steering input cost
                cost += u[k*2+1]**2*self.dt*100
            return cost

sim_run(options, ModelPredictiveControl)
