def fibinocci(n):
	if (n==0 or n==1):
		return  n
	else:
		return fibinocci(n-1)+fibinocci(n-2)
n=int(input("enter the number"))
for i in range(n):
	print(fibinocci(i))

