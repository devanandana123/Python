class rectangle:
	def __init__(self,length,breadth):
		self.breadth=breadth
		self.length=length
	def area(self):
		return self.breadth*self.length
	def perimeter(self):
		return 2*(self.breadth+self.length)
l=int(input("enter the length of the rectangle:"))
b=int(input("enter the breadth of the rectangle:"))		
object=rectangle(l,b)
print("Area of a rectangle :",object.area())
print("perimeter of a rectangle :",object.perimeter())
