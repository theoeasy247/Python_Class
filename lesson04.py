#def Lesson04 Exercise"
#reate a program that asks the user for:#

"===== PERSONAL INFORMATION ====="

name = input("Enter your name: ")
age = int(input("Enter your age: " ))
country = input("Enter your country: " )

print("===== PERSONAL INFORMATION =====")
print(f"Name = {name}")
print(f"Age = {age}")
print(f"Country = {country}")

# EXERCISE 2-Calculator

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))


print(f"Addition = {first_number + second_number}")
print(f"Subtraction = {first_number- second_number}")
print(f"multiplication = {first_number* second_number}")
print(f"Division = {first_number/second_number}")


# LESSON 4 CHALLENGE
# build a student average calculator

"===== STUDENT RESULT ====="
name = (input("Enter your name: "))
subjects = int(input("Enter your subjects: "))
total_marks = int(input("Enter total marks: "))

average =  total_marks / subjects

print("===== STUDENT RESULT =====")
print(f"Name =  {name}")
print(f"Subjects =  {subjects}")
print(f"Total  =  {total_marks}")
print(f"Average = {average}")
