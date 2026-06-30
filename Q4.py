# Marksheet Generation System

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- Marksheet -----")
print("Student Name :", name)
print("Roll Number  :", roll)
print("Total Marks  :", total, "/500")
print("Percentage   :", percentage, "%")
print("Grade        :", grade)

if grade == "F":
    print("Result       : Fail")
else:
    print("Result       : Pass")