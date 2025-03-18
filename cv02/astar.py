# A* sracka
import numpy as np
import pylab as plt

# set state space dimensions and start and goal position
dimension = 49
start = (1,1)
goal = (47,47)

# nahoru, dolu, doleva, doprava
actions = [(-1, 0), (1, 0), (0, 1), (0, -1)] 

def generate_maze(size, start, goal):
    """ TODLECTO MI NAPSAL CHAT, PREJ TO JE METODA REKURZIVNIHO BACKTRACKINGU PRO VYTVORENI BLUDISTE (???) BCS JSEM LINA A RUCNE TO DELAT NEBUDU """

    maze = np.ones(size, dtype=int)  # Všude nejdříve překážky (1)
    
    def carve(x, y):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        np.random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < size[0] - 1 and 1 <= ny < size[1] - 1 and maze[nx, ny] == 1:
                maze[nx - dx // 2, ny - dy // 2] = 0  # Odstraň stěnu
                maze[nx, ny] = 0  # Vytvoř cestu
                carve(nx, ny)
    
    # Start v levém horním rohu
    maze[1, 1] = 0
    carve(1, 1)
    # Nastavení startu a cíle jako průchozích míst
    maze[start[0], start[1]] = 0
    maze[goal[0], goal[1]] = 0
    
    return maze

def a_star(start, goal, state_space, actions, dimension):
    """ A STAR FUNKCE """

    # policko je dictionary s key = (x,y) a value = hodnota policka
    # kam muzu jet je open node
    # dictionary[key] = value
    open_nodes = {}
    g = {}
    visited = {}
    open_nodes[start] = 0
    g[start] = 0

# run loop until there are no open nodes
    while len(open_nodes) > 0:
        # toto mi vybere minimalni hodnotu values z open_nodes,
        # key=open_nodes.get mi rika podle jakeho argumentu to mam vybrat (tj. value)
        actual_state = min(open_nodes, key=open_nodes.get) 

        # delete actual node
        del open_nodes[actual_state]

        # check for goal
        if actual_state == goal:
            print(actual_state)
            return True, visited
        
        # node expansion
        for x, y in actions:
            new_state = actual_state[0] + x, actual_state[1] + y

            # check for wall/border
            if new_state[0] <0 or new_state[0] >= dimension or new_state[1] <0 or new_state[1]>=dimension or state_space[new_state[0], new_state[1]] == 1:
                continue

            # if the g value of one of the next nodes is higher than actual node
            if new_state not in g or g[new_state] > g[actual_state] + 1:

                # get g value
                g[new_state] = g[actual_state] + 1

                # get manhattan distance
                mnht = np.abs(goal[0] - new_state[0]) + np.abs(goal[1] - new_state[1])
                
                # add actual node to visited dict
                visited[new_state] = g[new_state] + mnht, actual_state

                # add new state to open nodes
                if new_state not in open_nodes:
                    open_nodes[new_state] = g[new_state] + mnht

                # dynamic plot
                for x,y in open_nodes.keys():
                    state_space[x,y] = 10
                
                state_space[start[0], start[1]] = 4
                state_space[goal[0], goal[1]] = 4

                # Update plot
                img.set_data(state_space)
                plt.draw()
                plt.pause(0.0001)  # Pause to show update
    return False, visited


"""
MAIN SHIT TUDUDUM
"""
state_space = generate_maze((dimension,dimension),start, goal)

# Create the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
img = ax.imshow(state_space, cmap="viridis", vmin=0, vmax=5)

# run the astar
r, visited = a_star(start, goal, state_space, actions, dimension)

# if there is a result, plot
if r == True:
    node = goal
    while node != start:
        f, prev_state = visited[node]
        print(prev_state)
        node = prev_state
        row, col = prev_state
        state_space[row,col] = 4

# draw result
img.set_data(state_space)
plt.ioff()  # Turn off interactive mode
plt.show()