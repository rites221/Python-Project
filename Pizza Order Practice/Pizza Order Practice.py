#Pizza Order

print("Welcome! Order the Pizza")

#using lower() to lower the characters, whether they are in capitals or lower.
Pizza_size = input("Do you want Small Pizza, Medium Pizza or Large Pizza? Enter the S, M or L:\n").lower()
Pizza_Pepperoni = input("Pepperoni For Small Pizza or For Medium or Large Pizza! Enter y or n\n").lower()
Pizza_cheese = input("Do you want extra cheese?Y or N\n").lower()

Bill = 0 

if Pizza_size == "s":
    Bill += 15
elif Pizza_size == "m":
    Bill += 20
elif Pizza_size == "l":
    Bill += 25

if Pizza_Pepperoni == "y":
    if Pizza_size == "s":
        Bill += 2
    else:
        Bill += 3

if Pizza_cheese == "y":
    Bill += 1


print(f"Your final bill is {Bill}")

