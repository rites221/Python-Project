#Averagae Height

St_height = input("Enter the list of height:").split()
for n in range(0, len(St_height)):
    St_height[n] = int(St_height[n])

total_height = 0
for height in St_height:
    total_height += height
print(f"total Height = {total_height}")

number_of_students = 0
for student in St_height:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height/number_of_students)
print(average_height)

