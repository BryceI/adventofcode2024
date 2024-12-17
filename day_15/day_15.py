inputlines = open('day_15/day_15_input.txt').read().splitlines()
print(inputlines)

map = []
moves = []
isMap = True
for line in inputlines:
    print(line)
    if len(line) == 0:
        print('switch')
        isMap = False
    if isMap:
        map.append(list(line))
    else:
        if len(line) > 0:
            moves.append(line)
print('map')
print(map)
print('moves')
print(moves)
moves = ''.join(moves)
print('==========================')
print(moves)

def get_starting_position(maze):
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == '@':
                return [x, y]
            
def print_map(map):
    for line in map:
        print(''.join(line))

starting_position = get_starting_position(map)
print("starting position", starting_position)

current_position = starting_position
for move in moves:
    pushedSomething = False
    print("move is ", move)
    if move == '^':
        current_x_to_check = current_position[0]-1
        current_y_to_check = current_position[1]
        current_tile_to_check = map[ current_x_to_check ][ current_y_to_check ]
        while current_tile_to_check == 'O':
            pushedSomething = True
            current_x_to_check = current_x_to_check - 1
            current_tile_to_check = map[ current_x_to_check ][ current_y_to_check ]
        if current_tile_to_check == '.':
            if pushedSomething:
                map[ current_x_to_check ][ current_y_to_check ] = 'O'
            map[ current_position[0] ][ current_position[1] ] = '.'
            map[ current_position[0] - 1 ][ current_position[1] ] = '@'
            current_position = [ current_position[0] - 1, current_position[1]]
        elif current_tile_to_check == '#':
            print('cant move')
        else:
            print("oops! 1")
    elif move == '>':
        current_x_to_check = current_position[0]
        current_y_to_check = current_position[1] + 1
        current_tile_to_check = map[ current_x_to_check ][ current_y_to_check ]
        while current_tile_to_check == 'O':
            pushedSomething = True
            current_y_to_check = current_y_to_check + 1
            current_tile_to_check = map[ current_x_to_check ][ current_y_to_check ]
        if current_tile_to_check == '.':
            if pushedSomething:
                map[ current_x_to_check ][ current_y_to_check ] = 'O'
            map[ current_position[0] ][ current_position[1] ] = '.'
            map[ current_position[0] ][ current_position[1] + 1 ] = '@'
            current_position = [ current_position[0], current_position[1] + 1]
        elif current_tile_to_check == '#':
            print('cant move')
        else:
            print("oops! 2" )
    elif move == 'v':
        current_x_to_check = current_position[0] + 1
        current_y_to_check = current_position[1]
        current_tile_to_check = map[ current_x_to_check ][ current_y_to_check ]
        while current_tile_to_check == 'O':
            pushedSomething = True
            current_x_to_check = current_x_to_check + 1
            current_tile_to_check = map[ current_x_to_check ][ current_y_to_check ]
        if current_tile_to_check == '.':
            if pushedSomething:
                map[ current_x_to_check ][ current_y_to_check ] = 'O'
            map[ current_position[0] ][ current_position[1] ] = '.'
            map[ current_position[0] + 1 ][ current_position[1] ] = '@'
            current_position = [ current_position[0] + 1, current_position[1]]
        elif current_tile_to_check == '#':
            print('cant move')
        else:
            print("oops! 3", current_tile_to_check)
    elif move == '<':
        current_x_to_check = current_position[0]
        current_y_to_check = current_position[1] - 1
        current_tile_to_check = map[ current_x_to_check ][ current_y_to_check ]
        print(current_x_to_check, current_y_to_check, current_tile_to_check)
        while current_tile_to_check == 'O':
            pushedSomething = True
            current_y_to_check = current_y_to_check - 1
            current_tile_to_check = map[ current_x_to_check ][ current_y_to_check ]
        print(current_x_to_check, current_y_to_check, current_tile_to_check)
        if current_tile_to_check == '.':
            if pushedSomething:
                map[ current_x_to_check ][ current_y_to_check ] = 'O'
            map[ current_position[0] ][ current_position[1] ] = '.'
            map[ current_position[0] ][ current_position[1] - 1 ] = '@'
            current_position = [ current_position[0], current_position[1] - 1]
        elif current_tile_to_check == '#':
            print('cant move')
        else:
            print("oops! 4", current_tile_to_check)
    else:
        print('oops 5')
    # print_map(map)

def calculateGPS(map):
    accum = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == 'O':
                accum += x * 100 + y
    return accum

print(calculateGPS(map))


#part 2
big_map = []
for line in map:
    new_line = []
    for cell in line:
        if 