inputlines = open('day_04/day_04_input.txt').read().splitlines()
print(inputlines)

line_length = len(inputlines[0])
num_lines = len(inputlines)

lines = []
for line in inputlines:
    lines.append( line + "." )
padded_line = "."*(len(lines[0]) + 1)
lines.append(padded_line)
print(lines)

#assume all lines equal length
x_range = line_length
y_range = num_lines
count = 0
for x in range(x_range):
    for y in range(y_range):
        # left = lines[y][x: x+4]
        # down = "".join([lines[y][x], lines[y+1][x], lines[y+2][x], lines[y+3][x]])
        if y > 0 and x > 0:
            diag_right = "".join([lines[y-1][x+1], lines[y][x], lines[y+1][x-1]])
            diag_left = "".join([lines[y-1][x-1], lines[y][x], lines[y+1][x+1]])
        else:
            diag_right = '...'
            diag_left = '...'
            
        # if left == 'XMAS' or left == "SAMX":
        #     print("left xmas at ", y, x)  
        #     count += 1
        # if down == 'XMAS' or down == "SAMX":
        #     print("down xmas at ", y, x)          
        #     count += 1
        if (diag_right == 'MAS' or diag_right == "SAM") and (diag_left == "MAS" or diag_left == "SAM"):
            print("found", y, x)
            count += 1
print(count)
