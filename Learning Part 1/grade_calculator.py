marks = input("Please enter your marks: ")# BuiltIn Funtion input()
marks = int(marks)# BuiltIn Funtion int()

if marks >= 80 :# if statement
    grade = "A+"
elif marks >= 70 :# elif statement
    grade = "A"
elif marks >= 60 :# elif statement
    grade = "A-"
elif marks >= 50 :# elif statement
    grade = "B"
else :# else statement
    grade = "F"

print("Your grade is ", grade)# Fianl Result

