marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))

total_marks = marks1 + marks2 + marks3
average = total_marks / 3

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Total Marks: {total_marks}")
print(f"Average: {average}")
print(f"Grade: {grade}")
