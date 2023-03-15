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


