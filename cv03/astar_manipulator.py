'''
ASTAR ALGORITHM FOR nxR MANIPULATOR
--------------------------------------------------------------
start   = ntice obsahujici pocatecni uhly ramen manipulatoru
goal    = ntice obsahujici koncove uhly ramen manipulatoru
x       = x souradnice prekazek
y       = y souradnice prekazek
--------------------------------------------------------------
f() = g() + h(), h() je rozdil uhlu pro kazdy prvek
'''

# import
import numpy as np
import pylab as plt
import utils03
from itertools import product
import time

arms = 2
arm_length = 80 # [px]
delta_phi = 1 # [°]

start = (50,120) # [°]
goal = (80,120) # [°]

state_space = [] # no obstacles

# makes every combination of actions for each arm
actions = [a for a in product([-delta_phi, 0, delta_phi], repeat=arms)]

r, visited = utils03.astar_manip(start, goal, state_space, actions, arm_length)

if r == True:
    node = goal

    x, y = [0], [0]

    plt.ion()

    # here we are creating sub plots
    fig, ax = plt.subplots()
    ax.set_xlim(-100, 100)  # Adjust as needed
    ax.set_ylim(-100, 100)  # Adjust as needed
    line, = ax.plot([], [], 'bo-')

    def update(x1,y1):
        line.set_data(x1)
        line.set_ydata(y1)
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.05)  # Control the speed of animation

    frame = 0
    while node != start:
        f, prev_state = visited[node]

        for i in range(len(node)):

            x1 = x[-1] + arm_length * np.cos(np.deg2rad(node[i]))
            y1 = y[-1] + arm_length * np.sin(np.deg2rad(node[i]))

            x.append(x1)
            y.append(y1)

        update(x1,y1)
        

        node = prev_state
