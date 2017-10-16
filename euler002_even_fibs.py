tot=0


#generate fib:


num2=0
fib=1
tot=0

while fib <= 4000000:

	num1=num2
	num2=fib
	print(fib)
	if fib%2==0:
		tot+=fib
	fib = num1+num2
print (tot)
