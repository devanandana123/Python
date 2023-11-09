def add(num1,num2):
	return num1+num2
def sub(num1,num2):
	return num1-num2
def mult(num1,num2):
	return num1*num2
def div(num1,num2):
	return num1/num2
def power(num1,num2):
	return num1**num2
def calculator(num1,operation,num2):
	if operation=="+":
		return add(num1,num2)
	elif operation=="-":
		return sub(num1,num2)
	elif operation=="*":
		return mult(num1,num2)
	elif operation=="/":
		return div(num1,num2)
	elif operation=="**":
		return power(num1,num2)
	else:
		print("invalid statement")
		
num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
operation=str(input("choose the operation +,-,*,/,**:"))
result = calculator(num1,operation,num2)
print("result",result)

