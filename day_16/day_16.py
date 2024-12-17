import pprint
from igraph import Graph

inputlines = open('day_16/day_16_input.txt').read().splitlines()
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
            if maze[x][y] == 'S':
                return [x, y]

def get_ending_position(maze):
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == 'E':
                return [x, y]

def print_map(map):
    for line in map:
        print(''.join(line))

starting_position = get_starting_position(map)
ending_position = get_ending_position(map)
print("starting position", starting_position)
print("ending position", ending_position)
print_map(map)

current_position = starting_position

nodes = {}
index = 0
#z -- 
# 0 = east
# 1 = south
# 2 = west
# 3 = north

directions = {
    0: '>',
    1: 'v',
    2: '<',
    3: '^'
}
for x in range(len(map) - 2):
    for y in range(len(map[0]) - 2):
        for z in range(4):
            curr_x = x+1
            curr_y = y+1
            if map[curr_x][curr_y] != '#':
                current_position = ','.join([str(curr_x), str(curr_y), directions[z]])
                nodes[current_position] = index
                index += 1
pprint.pp(nodes)

edges = []
weights = []
move_cost = 1
turn_cost = 1000
for x in range(len(map) - 2):
    for y in range(len(map[0]) - 2):
        for z in range(4):
            curr_x = x+1
            curr_y = y+1
            current_position = ','.join([str(curr_x), str(curr_y), directions(z)])
            turn_east_position = ','.join([str(curr_x), str(curr_y), directions('>')])
            turn_south_position = ','.join([str(curr_x), str(curr_y), directions('v')])
            turn_west_position = ','.join([str(curr_x), str(curr_y), directions('<')])
            turn_north_position = ','.join([str(curr_x), str(curr_y), directions('^')])
            east_position = ','.join([str(curr_x), str(curr_y + 1), '>'])
            south_position = ','.join([str(curr_x + 1), str(curr_y), 'v'])
            west_position = ','.join([str(curr_x), str(curr_y - 1), '<'])
            north_position = ','.join([str(curr_x - 1), str(curr_y), '^'])
            if map[curr_x][curr_y] != '#':

                #east
                if directions[z] == '>':
                    #look east
                    if map[curr_x][curr_y + 1] != '#':
                        edges.append([nodes[current_position], nodes[east_position]])
                        weights.append(move_cost)
                    #look south
                    if map[curr_x + 1][curr_y] != '#':
                        edges.append([nodes[current_position], nodes[turn_south_position]])
                        weights.append(turn_cost)
                    #look west
                    if map[curr_x][curr_y - 1] != '#':
                        edges.append([nodes[current_position], nodes[west_position]])
                        weights.append(move_cost)
                    #look north
                    if map[curr_x + 1][curr_y] != '#':
                        edges.append([nodes[current_position], nodes[turn_south_position]])
                        weights.append(turn_cost)
