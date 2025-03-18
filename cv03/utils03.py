import numpy as np
import time
import matplotlib.pyplot as plt

def astar_manip(start, goal, state_space, actions, arm_length):
    '''
    astar fcn for manipulator
    '''
    open_nodes = {}
    g = {}
    visited = {}
    open_nodes[start] = 0
    g[start] = 0

    while len(open_nodes) >0:

        actual_state = min(open_nodes, key=open_nodes.get) 

        del open_nodes[actual_state]

        # check for goal
        if actual_state == goal:
            print(actual_state)
            return True, visited
        
        # node expansion
        for action in actions:
            new_state = tuple(np.array(actual_state) + np.array(action))

            # check for wall/border
            # if new_state[0] <0 or new_state[0] >= dimension or new_state[1] <0 or new_state[1]>=dimension or state_space[new_state[0], new_state[1]] == 1:
            #     continue

            # if the g value of one of the next nodes is higher than actual node
            if new_state not in g or g[new_state] > g[actual_state] + 1:

                # get g value
                g[new_state] = g[actual_state] + 1
                mnht = 0

                # get manhattan distance
                for i in range(len(goal)):
                    mnht += np.abs(goal[i] - new_state[i])
                
                # add actual node to visited dict
                visited[new_state] = g[new_state] + mnht, actual_state

                # add new state to open nodes
                if new_state not in open_nodes:
                    open_nodes[new_state] = g[new_state] + mnht


    return False, visited
                       
