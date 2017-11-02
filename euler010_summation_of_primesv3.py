'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

http://www.binarycoder.org/math/sieve-of-eratosthenes/  (comments are mine)'''


max = 2000000

#create a list of all the numbers from 0 to max+1
lst = range(0, max + 1)

#second item set to zero (1 is not prime!)
lst[1] = 0


#only need to check those factors upto sqrt of max (+1)
thres = int(max**0.5) + 1


for i in range(2, thres):


	if lst[i] == 0:
		continue


#iterate over the numbers in the 'i' times table and set to zero (can't be prime if in 'i' times table!)
#start at i*i
	for j in range(i * i, len(lst), i):
		if lst[j] != 0:
			lst[j] = 0
#print ([i for i in lst if i != 0])
print(sum(lst))
