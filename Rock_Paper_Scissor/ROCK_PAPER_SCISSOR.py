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

You_Choose = (input("What do you want to choose? Enter 0 for Rock, 1 for Paper or 2 for Scissors\n")).lower()
list_Choice = [rock, paper, scissors]
Computer_Chooses = random.randint(0,2)
print("Computer Choose:")
print(You_Choose[Computer_Chooses])


if You_Choose >= 2 or You_Choose < 0:
    print("You typed an invalid number, you loose")
elif You_Choose == 0 and Computer_Chooses == 2:
    print("You win")
elif Computer_Chooses == 2 and You_Choose == 0:
    print("You Loose")
elif Computer_Chooses > You_Choose:
    print("You loose")
elif You_Choose > Computer_Chooses:
    print("You win")
elif Computer_Chooses == You_Choose:
    print("It's a tie")


#2nd code

Your_Choice = input("What Do you want to choose?\nRock, Paper, Scissors\n").lower()
list_R_P_S = ["Rock","Paper","Scissors"]
Computer_Chooses = (random.choice(list_R_P_S)).lower()
print(Computer_Chooses)
if Your_Choice == "rock" and Computer_Chooses == "paper":
    print("You Loose, Computer Wins")
elif Your_Choice == "paper" and Computer_Chooses == "scissors":
    print("You Loose, Computer Wins")
elif Your_Choice == "scissors" and Computer_Chooses == "rock":
    print("You Loose, Computer Wins")
elif Your_Choice == Computer_Chooses:
    print("It's a draw")
elif Your_Choice == "paper" and Computer_Chooses == "rock":
    print("You Won")
elif Your_Choice == "scissors" and Computer_Chooses == "paper":
    print("You Won")
elif Your_Choice == "Scissors" and Computer_Chooses == "rock":
    print("You Won")

