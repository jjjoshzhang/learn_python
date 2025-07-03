import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if num == 0:
    h_choice = rock
    print(h_choice)
    print("Computer Chose: ")
    RPC = [rock, paper, scissors]
    c_choice = random.choice(RPC)
    print(c_choice)
    if c_choice == rock:
        print("It's a draw")
    elif c_choice == scissors:
        print("You win")
    else:
        print("You lose")

elif num == 1:
    h_choice = paper
    print(h_choice)
    print("Computer Chose: ")
    RPC = [rock, paper, scissors]
    c_choice = random.choice(RPC)
    print(c_choice)
    if c_choice == paper:
        print("It's a draw")
    elif c_choice == rock:
        print("You win")
    else:
        print("You lose")

else:
    h_choice = scissors
    print(h_choice)
    print("Computer Chose: ")
    RPC = [rock, paper, scissors]
    c_choice = random.choice(RPC)
    print(c_choice)
    if c_choice == scissors:
        print("It's a draw")
    elif c_choice == paper:
        print("You win")
    else:
        print("You lose")
