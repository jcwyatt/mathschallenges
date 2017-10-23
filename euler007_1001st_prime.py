'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

primes=[2,3]
i=5
while len(primes) != 10001:

	'''increase the start number by one each time 
	(or 2 since we only need odds)
	for each number go back down through the other numbers 
	and see which ones have no factors but 1'''

	j=int(i//2)-1	#start with divisor half-1 of the current test number

	while j!=1:
		if i%j==0:  
			break 	#end while loop
		else:
			j-=1
	if j==1:
		primes.append(i)
		print(i)
		i+=2
	else:
		i+=2

print (primes)

'''took 350s !!!!'''










