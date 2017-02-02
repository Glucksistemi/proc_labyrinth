import random
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

    def get_path_values():
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
    lmap = [[EMPTY for w in range(y)] for h in range(x)]
    # creating path
    directions = [
        {'swap': 1, 'add':-1},
        {'swap': 0, 'add': 1},
        {'swap': 1, 'add': 1},
        {'swap': 0, 'add':-1}
    ]
    path_start = random.randint(0,y-1)
    path_pos = [0,path_start]
    direction = -1
    while not '=' in lmap[x-1]:
        #os.system('cls')
        #show_matrix(lmap)
        direction = choose_direction(path_pos)
        pmin, pmax = get_path_values()
        path_line_length = random.randint(pmin, pmax)
        #print path_line_length, direction
        for p in range(path_line_length):
            lmap[path_pos[0]][path_pos[1]] = PATH
            if path_pos[directions[direction]['swap']] != checkway():
                path_pos[directions[direction]['swap']] += directions[direction]['add']
                #print path_pos, direction
            else:
                break
    lmap[0][path_start] = START
    # building walls
    for i in range(len(lmap)):
        for j in range(len(lmap[i])):
            if i > 2 and (lmap[i][j-1] != 'X' or lmap[i-1][j] != 'X'):
                chance = 50
            else:
                chance = 80
            if rand_bool(chance) and lmap[i][j] == ' ':
                lmap[i][j] = 'X'
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

lmap = create_level_map(80,30)
show_matrix(lmap)