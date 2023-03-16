
#Banker Roulette
import random

names_string = input("Enter your name of the people on the table:")
names_split = names_string.split()
no_of_people = len(names_split)
random_name = random.randint(0, no_of_people -1)
payee = names_split[random_name]
print(random_name)