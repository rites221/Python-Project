#Days, Weeks, Months we have left if we live until 80 years old.
Age = int(input("Enter your current age: "))

Days_In_Year = 365
Weeks_In_Year = 52
Months_In_Year = 12

Years_Left = 80 - int(Age)

Days_Left = Years_Left*Days_In_Year
Weeks_Left = Years_Left*Weeks_In_Year
Months_Left = Years_Left*Months_In_Year

print(f"You have {Months_Left} Months, {Weeks_Left} Weeks and {Days_Left} Days to live the life, So live happily")


