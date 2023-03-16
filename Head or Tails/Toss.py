print("\tIt's time for toss")

import random #importing random to randomly pick the values out of two
Toss_Time = ['heads', 'tails']
Computer_Chooses = random.choice(Toss_Time)
Choose_Your_Side = input("What do you want? Heads or Tails\n").lower()

if Choose_Your_Side == Computer_Chooses:
    print(f"It's {Computer_Chooses} You Won.")
else:
    print(f"It's {Computer_Chooses} You Loose. Computer wins")