# input the marks of respective subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))
subject4 = float(input("Enter marks for Subject 4: "))

average_marks = (subject1 + subject2 + subject3 + subject4) / 4

passing_grade_required = 35

if average_marks >= passing_grade_required:
    result = "Pass"
else:
    result = "Fail"

print(f"Average Marks: {average_marks}")
print(f"Result: {result}")