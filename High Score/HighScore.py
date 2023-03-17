#High Score

Score_List = input("Enter the Scores:").split()

for n in range(0, len(Score_List)):
    Score_List[n] = int(Score_List[n])

highest_score = 0
for score in Score_List:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
