import random

#params


PATH = '='
START = 'S'
WALL = 'X'
EMPTY = ' '


def rand_bool(chance):
    return random.randint(0,100) < chance


def create_level_map(x, y):
    xy = (x, y)

    def choose_direction(pos):
        if pos[0] == 0:
            if pos[1] == 0:
                dirs = [1, 2]
            elif pos[1] == y - 1:
                dirs = [1, 0]
            else:
                dirs = [1, 2, 0]
        else:
            if pos[1] == 0:
                dirs = [1, 2, 3]
            elif pos[1] == y - 1:
                dirs = [1, 2, 0]
            else:
                dirs = [0,1,2,3]
        if direction in (0,2):
            try:
                dirs.pop(dirs.index(2))
                dirs.pop(dirs.index(0))
            except (IndexError, ValueError):
                pass
        elif direction in(1,3):
            try:
                dirs.pop(dirs.index(1))
                dirs.pop(dirs.index(3))
            except (IndexError, ValueError):
                pass
        return random.choice(dirs)

    def get_path_values(): # min and max lengths of the path straight fragment depending on direction
        if direction == 3:
            return 1,3
        if direction == 1:
            return 5,8
        if direction in (0,2):
            return 3,10

    def checkway():
        if directions[direction]['add'] == -1:
            return 0
        else:
            return xy[directions[direction]['swap']]-1
    lmap = [[EMPTY for w in range(y)] for h in range(x)] # THE CREATION OF MATRIX
    # creating path
    directions = [ # posible direction of movement
        {'swap': 1, 'add':-1}, # up (y-)
        {'swap': 0, 'add': 1}, # right (x+)
        {'swap': 1, 'add': 1}, # down (y+)
        {'swap': 0, 'add':-1}  # left (x-)
    ]
    path_start = random.randint(0,y-1) # random start point on the left side of field
    path_pos = [0,path_start]
    direction = -1 # direction will be reseted anyway, but it should have initial value
    while not PATH in lmap[x-1]:
        direction = choose_direction(path_pos)
        pmin, pmax = get_path_values()
        path_line_length = random.randint(pmin, pmax) # straight line length
        for p in range(path_line_length):
            lmap[path_pos[0]][path_pos[1]] = PATH # marking up an map block as path block
            if path_pos[directions[direction]['swap']] != checkway(): # ceeping path from geting out of map
                path_pos[directions[direction]['swap']] += directions[direction]['add'] # moving towards chosen direction
            else:
                break
    lmap[0][path_start] = START
    # building walls
    for i in range(len(lmap)):
        for j in range(len(lmap[i])):
            if i > 2 and (lmap[i][j-1] != WALL or lmap[i-1][j] != WALL):
                chance = 50 # if there is no wall nearby - less chance to create other wall
            else:
                chance = 80
            if rand_bool(chance) and lmap[i][j] == EMPTY: # wall cannot be set on the path
                lmap[i][j] = WALL
    # removing path
    for i in range(len(lmap[0])):
        for j in range(len(lmap)):
            if lmap[j][i] == PATH:
                lmap[j][i] = EMPTY
    return lmap


def show_matrix(matrix):
    for i in range(len(matrix[0])):
        print '[',
        for j in range(len(matrix)):
            print matrix[j][i],
        print ']'

# lmap = create_level_map(80,30)
# show_matrix(lmap)