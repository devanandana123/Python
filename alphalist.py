a=int(input("enter the number of list to be displayed:"))
name=[]
for i in range (0,a):
	names=input("enter the name:")
	name.append(names)
print("\n elements in the list are:",name)
print("\n sorted elements in list are:")
for i in sorted(name):
	print(i)
