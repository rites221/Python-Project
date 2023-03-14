#BMI Calculator

print("BMI Calculator")
Weight = float(input("Enter your weight(in Kg):")) #80
Height = float(input("Enter your height(in meters):")) #1.8

Calculate_BMI = (Weight)/(Height*Height)
# print(Calculate_BMI) #24.691358024691358

#round off the value
round_off_value = print(round(Calculate_BMI)) #round() function will round off the value to 25.
print(round_off_value)