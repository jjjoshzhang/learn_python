import art
import random
import game_data

def generate():
    return random.choice(game_data.data)

def ask(a, b):
    compare = 'Compare A'
    against = 'Against B'

    print(f"{compare}: {a['name']}, a/an {a['description']}，from {a['country']}")

    print(art.vs)
    print(f"{against}: {b['name']}, a/an {b['description']}，from {b['country']}")
    check(a, b)



def winner(a,b):
    if a['follower_count'] < b['follower_count']:
        return 'b'
    if a['follower_count'] > b['follower_count']:
        return 'a'
    return False


def check(a,b):
    global score
    ans = winner(a,b)
    inp = input("Who has more followers? Type 'A' or 'B': ").lower()
    if inp == ans:
        score += 1
        print("\n" * 20)
        print(art.logo)
        print(f'You are right, your current score is: {score}')
        correct(a, b)
    else:
        print("\n" * 20)
        print(art.logo)
        print('You got it wrong!')
        quit()


def correct(a,b):
    if int(a['follower_count']) > int(b['follower_count']):
        b = generate()
        different(a,b)
        ask(a,b)
    if int(a['follower_count']) < int(b['follower_count']):
        a = b
        b = generate()
        different(a,b)
        ask(a,b)


def different(a,b):
    gg = True
    while gg:
        if a['name'] == b['name']:
            b = random.choice(game_data.data)
            gg = True
        elif b['name'] != a['name']:
            gg = False


score = 0
rand1 = random.choice(game_data.data)
rand2 = random.choice(game_data.data)
different(rand1,rand2)
print(art.logo)
print(f"Compare A: {rand1['name']}, a/an {rand1['description']}，from {rand1['country']}")
print(art.vs)
print(f"Against B: {rand2['name']}, a/an {rand2['description']}，from {rand2['country']}")
check(rand1,rand2)