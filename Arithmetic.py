a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
operation=("choose an arithmetic operations(*,/,-,+,//,%)")
if operation =="+":
    result=a+b
elif operation =="-":
    result=a-b
elif operation =="*":
    result=a*b
elif operation =="/":
    result=a/b
elif operation =="//":
    result=a//b
elif operation =="%":
    result=a%b
else:
    print("invalid")
print("result of the arithmetic operation", result )
