MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins ={
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}



def report(resource,profit):
    print(f"Water: {resource['water']}ml\n"
          f"Milk: {resource['milk']}ml\n"
          f"Coffee: {resource['coffee']}g\n"
          f"Money: ${profit}")

def calc(q,d,n,p,c):
    return q*c['quarters'] + d*c['dimes'] + n*c['nickels'] + p*c['pennies']




def espresso(a,c):
    global money,drink_names
    q = float(input("how many quarters?: "))
    d = float(input("how many quarters?: "))
    n = float(input("how many quarters?: "))
    p = float(input("how many quarters?: "))
    moneyt = calc(q,d,n,p,c)
    if a['espresso']['cost'] > moneyt:
        print("Sorry, that's not enough money. Money refunded.")
    elif a['espresso']['cost'] < moneyt:
        moneyrf = moneyt - a['espresso']['cost']
        money += a['espresso']['cost']
        print(f"Here is ${moneyrf:.2f} in change."
              "Here is your espresso ☕️. Enjoy!")
        makecoffe(a,drink_names[0])


def latte(a,c):
    global money,drink_names
    q = float(input("how many quarters?: "))
    d = float(input("how many quarters?: "))
    n = float(input("how many quarters?: "))
    p = float(input("how many quarters?: "))
    moneyt = calc(q, d, n, p, c)
    if a['latte']['cost'] > moneyt:
        print("Sorry, that's not enough money. Money refunded.")
    elif a['latte']['cost'] < moneyt:
        moneyrf = moneyt - a['latte']['cost']
        money += a['latte']['cost']
        print(f"Here is ${moneyrf:.2f} in change."
              "Here is your latte ☕️. Enjoy!")
        makecoffe(a,drink_names[1])

def cappuccino(a,c):
    global money,drink_names
    q = float(input("how many quarters?: "))
    d = float(input("how many quarters?: "))
    n = float(input("how many quarters?: "))
    p = float(input("how many quarters?: "))
    moneyt = calc(q, d, n, p, c)
    if a['cappuccino']['cost'] > moneyt:
        print("Sorry, that's not enough money. Money refunded.")
    elif a['cappuccino']['cost'] < moneyt:
        moneyrf = moneyt - a['cappuccino']['cost']
        money += a['cappuccino']['cost']
        print(f"Here is ${moneyrf:.2f} in change."
              "Here is your cappuccino ☕️. Enjoy!")
        makecoffe(a,drink_names[2])


def makecoffe(a,n):
    global resources
    resources['water'] -= a[n]['ingredients']['water']
    resources['milk'] -= a[n]['ingredients']['milk']
    resources['coffee'] -= a[n]['ingredients']['coffee']





money = 0
drink_names = list(MENU.keys())
over = True
while over:
    ans = input(f"What would you like? ({drink_names[0]}/{drink_names[1]}/{drink_names[2]}): ").lower()
    if ans == 'report':
        report(resources,money)
    elif ans == 'off':
        over = False
    elif ans == drink_names[0]:
        espresso(MENU,coins)
    elif ans == drink_names[1]:
        latte(MENU,coins)
    elif ans == drink_names[2]:
        cappuccino(MENU,coins)
