first=input("enter first no :")
second=input("enter second no :")
operator=input("enter operator(+,-,*,/,%) :")

first=int(first)
second=int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("enter valid operator")