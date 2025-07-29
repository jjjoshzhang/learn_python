
import art
import random





def easy(numr):
    lives = 10
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number. ")
        guess = int(input("Make a guess: "))
        lives = rangee(numr,guess,lives)
    print(f"You ran out of guesses, you lose! The correct answer is :{numr}")


def hard(numr):
    lives = 5
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number. ")
        guess = int(input("Make a guess: "))
        lives = rangee(numr,guess,lives)
    print(f"You ran out of guesses, you lose! The correct answer is : {numr}")


def rangee(num,numg,att):
    if num < numg:
        print("Too High\n"
              "Guess again")
        att -= 1
        return att
    elif num > numg:
        print("Too Low\n"
              "Guess again")
        att -=1
        return att
    elif num == numg:
        print(f"You guessed it right! The number is: {num}!")
        att = 0
        return att
    return att


print(art.logo)
print("Welcome to the Number Guessing Game!\n"
      "I'm thinking a number between 1 and 100")
random_num = random.randint(1,100)
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == "easy":
    easy(random_num)
elif level == "hard":
    hard(random_num)
else:
    print("Invalid Input")
    quit()

