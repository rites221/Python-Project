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

You_Choose = (input("What do you want to choose? Rock, Paper or Scissors\n")).lower()
print_Choice = [rock, paper, scissors]
Computer_Chooses = random.choice(print_Choice)
print(Computer_Chooses)