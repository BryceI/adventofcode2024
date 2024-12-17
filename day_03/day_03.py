import re

lines = open('day_03/day_03_input.txt').read()
regex = re.compile('(mul\(\d+\,\d+\)|do\(\)|don\'t\(\))')
muls = re.findall(regex, lines)
regex2 = re.compile('\d+')
accum = 0
enabled = True
for mul in muls:
    if mul == 'do()':
        enabled = True
    elif mul == "don't()":
        enabled = False
    else:
        vals = re.findall(regex2, mul)
        if enabled:
            accum += int(vals[0]) * int(vals[1])
print ( accum )