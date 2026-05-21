n = int(input())
for _ in range(n):
    x=input()
    y=x.split()
    number1=float(y[1])
    number2=float(y[3])
    operator=y[2]
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        result = number1 / number2
    print(result)