class Node:
    def __init__(self, x: int, y: int, plant, edges):
        self.x = x
        self.y = y
        self.plant = plant

input = open('day_12/day_12_input_small.txt').read().splitlines()
height = len(input)
width = len(input[0])
print (height, width)


# print(input)
graph = {}

for x in range(height):
    for y in range(width):
        graph[(x,y)] = input[x][y]


print(graph)
