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

