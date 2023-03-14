#Tip Calculator

Currency = input(("Enter the Currency:")) #$
Total_Bill = int(input(f"Enter the total Bill:{Currency}")) #1000
Total_People = int(input("Enter the Total Number of People:")) #21
Total_Tip = int(input("Enter the percentage of tip you want to pay:")) #10
Total_Tip_per = Total_Tip/100

Each_Person_Should_Pay = (Total_Bill/Total_People)*Total_Tip_per + Total_Bill/Total_People #52.38095238095238 
round_off_payment = round(Each_Person_Should_Pay, 2)
print(f"Each Person Should Pay {round_off_payment}") #52.38