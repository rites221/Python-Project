# Treasure Island Game

print("Welcom to Treasure Island. Your Mission is to Find the treasure!")
Start_the_game = input("Choose Left or Right: ").lower()


if Start_the_game == "left":
    Swim_wait = input("Do you want to swim accross the river or wait: ").lower()
    if Swim_wait == "wait":
        Which_Door = input("Which door do want to enter? Blue, Red, Yellow: ").lower()
        if Which_Door == "yellow":
            print("You win")
        elif Which_Door == "Red":
            print("Burned By Fire. Game Over")
        elif Which_Door == "Blue":
            print("Eaten By Beasts. Game Over")
        else:
            print("Game Over")
    else:
        print("Attacked By Trout.Game Over")
else:
    print("Fall into a hole. Game Over")

#Treasure Island Game Using If and Else Loop

print("Welcome to the treasure island\nYour duty is to find the treasure")

Start_game = input("You are at crossroads. Where do you want to go 'Right' or 'Left'\n").lower()
if Start_game == 'left':
    Swim_wait = input('What do you want to do now? Swim or Wait\n').lower()
    if Swim_wait == 'wait':
            Blue_Green_Red = input('Choose the door-Red, Blue, Green\n')
            if Blue_Green_Red == 'red':
                print("You Won")
            else:
                print('Sorry, You lose')
    else:
        print('Sorry, You lose')

else:
    print('Sorry, You lose')


