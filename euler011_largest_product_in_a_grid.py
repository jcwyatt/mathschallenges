import re
with open('euler011numbers.txt') as f:
	rawgrid = f.read()

strgrid = re.split('\W',rawgrid)

grid = [int(number) for number in strgrid]

print (grid[0], grid[20])