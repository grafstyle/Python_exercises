import random

print("Welcome to the best rock papel & scissors game")
print("")

user_choose = ''

def game(user_choose):
    pc_choose = ''
    pc_wins = 0
    user_wins = 0
    while pc_wins != 3 or user_wins != 3:
        user_choose = int(input("choose Rock (1), Papel (2) or Scissors (3): "))
        pc_choose = random.randint(1, 3)
        if user_choose == pc_choose:
            print("Tie")
        elif user_choose == 1 and pc_choose == 3:
            print("You win this match!")
            user_wins += 1
        elif user_choose == 2 and pc_choose == 1:
            print("You win this match!")
            user_wins += 1
        elif user_choose == 3 and pc_choose == 2:
            print("You win this match!")
            user_wins += 1
        else: 
            print("You lose this match.")
            pc_wins += 1
    if user_wins == 3:
        print("YOU ARE A WINNER!")
    else:
        print("You lose, try again")
        
        
game(user_choose)