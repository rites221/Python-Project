#Tip Calculator

Currency = input(("Enter the Currency:")) #$
Total_Bill = int(input(f"Enter the total Bill:{Currency}")) #1000
Total_People = int(input("Enter the Total Number of People:")) #21
Total_Tip = int(input("Enter the percentage of tip you want to pay:")) #10
Total_Tip_per = Total_Tip/100

Each_Person_Should_Pay = (Total_Bill/Total_People)*Total_Tip_per + Total_Bill/Total_People #52.38095238095238 
round_off_payment = round(Each_Person_Should_Pay, 2)
print(f"Each Person Should Pay {round_off_payment}") #52.38

#Tip Calculator

print("Welcome to the tip calculator")
Bill = int(input("What is the total bill\n$ "))
Total_People = int(input('Total Number of people\n'))
Pay_Tip = input("Do you want to pay the tip?\nYes/No ").lower()

if Pay_Tip == 'yes':
    Tip_Percentage = int(input("What percentage of the total bill would you like to give as a tip? 10,12 Or 15\n"))
    if Tip_Percentage == 10:
        Bill_1 = ((Bill+Bill * 0.10)/Total_People)
        print(f"Each Person Should Pay {Bill_1}")
    elif Tip_Percentage == 12:
        Bill_2 = ((Bill+Bill * 0.12) / Total_People)
        print(f"Each Person Should Pay {Bill_2}")
    elif Tip_Percentage == 15:
        Bill_3 = ((Bill+Bill * 0.15)/Total_People)
        print(f"Each Person Should Pay {Bill_3}")
else:
    Bill_0 = (Bill/Total_People)
    print(f"Your Total Bill is {Bill}.Each person Should pay {Bill_0}.Thank you for visiting. Visit us again!. Have a great day ahead")
