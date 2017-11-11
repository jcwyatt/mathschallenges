import re
from time import sleep

with open('euler011numbers.txt') as f:
	rawgrid = f.read()

strgrid = re.split('\W',rawgrid)

grid = [int(number) for number in strgrid]

print (grid[0], grid[20])

biggestProduct = 0

for locn,num in enumerate (grid):
	#vertical rows
	if locn<340:
		currentProduct = num*grid[locn+20]*grid[locn+40]*grid[locn+60] 
		if currentProduct>biggestProduct:
			biggestProduct = currentProduct
		print(biggestProduct)
	#backslashes
	if locn%20<17 and locn<340:
		currentProduct = num*grid[locn+21]*grid[locn+42]*grid[locn+63] 
		if currentProduct>biggestProduct:
			biggestProduct = currentProduct
		print(locn, num)
		print(biggestProduct)
		
	#fwdslashes
