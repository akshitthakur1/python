a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter the operator: ")
if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Invalid operator")