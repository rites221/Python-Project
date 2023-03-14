#BMI Calculator

print("BMI Calculator")
Weight = float(input("Enter your weight(in Kg):")) #80
Height = float(input("Enter your height(in meters):")) #1.8

Calculate_BMI = (Weight)/(Height*Height)
Calculate_BMI_Roundoff = round(Calculate_BMI)
# print(Calculate_BMI) #24.691358024691358

if Calculate_BMI < 18.5:
    print(f"Your BMI is {Calculate_BMI_Roundoff}, You are underweight")
elif Calculate_BMI > 18.5 and Calculate_BMI <= 25 :
    print(f"Your BMI is {Calculate_BMI_Roundoff}, You are normal weight")
elif Calculate_BMI > 25 and Calculate_BMI <= 30:
    print(f"Your BMI is {Calculate_BMI_Roundoff}, You are slightly overweight")
elif Calculate_BMI >30 and Calculate_BMI <= 35:
    print(f"Your BMI is {Calculate_BMI_Roundoff}, You are Obsese")
elif Calculate_BMI > 35 :
    print(f"Your BMI is {Calculate_BMI_Roundoff},you are clinically obese")
