string=input("enter string: ")
print("the string before replacing:",string)
x=string[0]
replaced=x+string[1:].replace(x,"$")
print("the string afer replacing is :",replaced)
