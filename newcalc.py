

num1 = float(input("Enter the number : "))
op = input("Enter the operator : ")
num2 = float(input("Enter the second number : " )) 

if op == "+" :
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/" :
    print(num1/num2)
elif op == "*":
    print(num1*num2)
elif op == "^":
    print(num1*int(num2))
else:
    print("Invalid Operator")

