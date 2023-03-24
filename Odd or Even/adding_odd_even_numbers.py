#Adding odd and even number

number_1 = int(input("enter the number upto where you want to calculate even numbers: "))

sum = 0
for even in range(0, number_1+1):
    if even % 2 == 0:
        sum += even
    print(sum)
