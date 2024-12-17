inputlines = open('day_06/day_06_input_small.txt').read().splitlines()
print(inputlines)

def get_starting_position(maze):
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == '^':
                return [x, y]

starting_position = get_starting_position(inputlines)
starting_position.append('^')
print("starting position", starting_position)

current_position = starting_position

def isValidPosition(position, maze):
    x, y, d  = position
    if x >= 0 and x < len(maze):
        if y >= 0 and y < len(maze[0]):
            return True
    return False
visitedPositions = {}
listOfObstacles = []

while isValidPosition(current_position, inputlines):
    x, y, d = current_position
    current_location = ",".join([str(current_position[0]), str(current_position[1])])
    if current_location not in visitedPositions:
        visitedPositions[current_location] = 0
    visitedPositions[current_location] += 1
    if d == '^':
        if x > 0 and inputlines[x-1][y] == '#':
            listOfObstacles.append(current_position)
            new_d = '>'
            new_x = x
            new_y = y
        else:
            new_d = '^'
            new_x = x-1
            new_y = y
        new_position = [new_x, new_y, new_d]

    elif d == '<':
        if y > 0 and inputlines[x][y-1] == '#':
            listOfObstacles.append(current_position)
            new_d = '^'
            new_x = x
            new_y = y
        else:
            new_d = '<'
            new_x = x
            new_y = y - 1
        new_position = [new_x, new_y, new_d]
    elif d == 'v':
        if x < len(inputlines) - 1 and inputlines[x+1][y] == '#':
            listOfObstacles.append(current_position)
            new_d = '<'
            new_x = x
            new_y = y
        else:
            new_d = 'v'
            new_x = x + 1
            new_y = y
        new_position = [new_x, new_y, new_d]
    elif d == '>':
        if y < len(inputlines[0]) - 1 and inputlines[x][y + 1] == '#':
            listOfObstacles.append(current_position)
            new_d = 'v'
            new_x = x
            new_y = y
        else:
            new_d = '>'
            new_x = x
            new_y = y + 1
        new_position = [new_x, new_y, new_d]
    else:
        print('oops')
    current_position = new_position
print (len(visitedPositions))
print (listOfObstacles)
count_of_possible_loops = 0
for i in range (len(listOfObstacles) - 3):
    if listOfObstacles[i][2] == '^':
        if listOfObstacles[i+3][1] < listOfObstacles[i][1]:
            print("found loop at ", listOfObstacles[i])
            count_of_possible_loops += 1
    if listOfObstacles[i][2] == '>':
        if listOfObstacles[i+3][0] < listOfObstacles[i][0]:
            print("found loop at ", listOfObstacles[i])
            count_of_possible_loops += 1
    if listOfObstacles[i][2] == 'v':
        if listOfObstacles[i+3][1] > listOfObstacles[i][1]:
            print("found loop at ", listOfObstacles[i])
            count_of_possible_loops += 1
    if listOfObstacles[i][2] == '<':
        if listOfObstacles[i+3][0] > listOfObstacles[i][0]:
            print("found loop at ", listOfObstacles[i])
            count_of_possible_loops += 1
print(count_of_possible_loops)