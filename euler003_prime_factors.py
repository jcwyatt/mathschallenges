'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

max = 600851475143

factors=[]

for i in range (1,int((max**0.5)+1)):
	if max%i==0:
		print(i)
		factors.append(i)

for i in factors[::-1]:
	for j in factors:
		print(i,"/",j,"=",i/j)

#cheated and looked at results of this print to find the largest prime factor.
