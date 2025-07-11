import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def multiply(n1,n2):
    return n1 * n2

def division(n1,n2):
    return n1 / n2

def minus(n1,n2):
    return n1 - n2


num1 = float(input("What's the first number?: "))
operation = input("+\n-\n*\n/\nPick an operation: ")
num2 = float(input("What's the next number: "))

if operation == "*":
    ans = multiply(num1,num2)
elif operation == "+":
    ans = add(num1,num2)
elif operation == "-":
    ans = minus(num1,num2)
elif operation == "/":
    ans = division(num1,num2)
else:
    print("Invalid")
