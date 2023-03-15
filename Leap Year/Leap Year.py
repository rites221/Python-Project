#Leap Year

print("\tLeap Year")

Year = int(input("Enter the Year: "))

if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("The Year is Leap Year")
        else:
            print("The year is not a leap year")
    else:
        print("The Year is a Leap Year")
else:
    print("The Year is not a leap year")
