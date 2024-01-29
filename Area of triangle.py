print("Area of a triangle")
a=int(input("Enter the side a: "))
b=int(input("Enter the side b:"))
c=int(input("Enter the side c:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of a triangle:",area)
