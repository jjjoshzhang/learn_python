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

operation_dic ={
    "+" : add,
    "-" : minus,
    "*" : multiply,
    "/" : division,

}

def calculation():
    num1 = float(input("What's the first number?: "))
    cont = True
    while cont:
        operation = input("+\n-\n*\n/\n Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        ans = operation_dic[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {ans}")
        y_n = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation. ")
        if y_n == "y":
            num1 = ans
        elif y_n =="n":
            cont = False
            print("\n"*20)
            print(art.logo)
            calculation()

calculation()
