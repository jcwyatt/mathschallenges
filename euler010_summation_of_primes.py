'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

max = 200000
numbs = [2]
for i in range (3,max,2):
	numbs.append(i)
print (len(numbs))


posn = 1
i=numbs[posn]

while i < (int((max**0.5)+1)):
	i=numbs[posn]
	#pop off all the numbers divisible by i
	print(i)
	for num in numbs:
		if num%i ==0 and num!=i:
			numbs.remove(num)
	posn+=1

print(sum(numbs))


