print("swapping by using temporary value")
a=5
b=10
print("a before swapping ",a)
print("b before swapping ",b)
temp=a
a=b
b=temp
print("a after swapping ",a)
print("b after swapping",b)
print("swapping without using temporary value")
a=3
b=7
print("a before swapping:",a)
print("b before swapping:",b)
a=a+b
b=a-b
a=a-b
print("a after swapping ",a)
print("b after swapping",b)
