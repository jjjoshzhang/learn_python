import art
import random

def checkbj(num1):
    for n in num1:
        if n == 10 or n ==11:
            return True
    return False
def win_or_lose(sh,sc,ch,cn):
    if sh > 22:
        print("Busted, Computer win!")
    elif sc > 22:
        print("Busted, You win!")
    elif checkbj(cn):
        print("Computer win with blackjack")
    elif checkbj(ch):
        print("You win with blackjack")
    elif sc < sh:
        print("You win")
    elif sh < sc:
        print("Computer win")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
gg = True
while gg:
    y_or_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if y_or_no == 'y':
        print("\n"*20)
        print(art.logo)
        score = 0
        score_c =0
        human_numbers = random.sample(cards,2)
        for num in human_numbers:
                score += num
        print(f"Your cards: {human_numbers}, current score: {score}")
        com_numbers = random.sample(cards,2)
        print(f"Computer's first card is: {com_numbers[0]}")
        y_or_no = input("Type 'y' to get another card, type 'n' to pass.").lower()
        if y_or_no == 'y':
            human_numbers += random.sample(cards,1)
            score = sum(human_numbers)
            score_c = sum(com_numbers)
            print(f"Your cards: {human_numbers}, final score: {score}")
            print(f"Computer's final hand is :{com_numbers}, final score: {score_c}")
            win_or_lose(score,score_c,human_numbers,com_numbers)

        else:
            com_numbers += random.sample(cards,1)
            score_c = sum(com_numbers)
            print(f"Your cards: {human_numbers}, final score: {score}")
            print(f"Computer's final hand is :{com_numbers}, final score: {score_c}")
            win_or_lose(score,score_c,human_numbers,com_numbers)
    else:
        quit()