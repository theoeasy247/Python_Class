#python
age = int(input("Enter your age: "))
has_id = input("Enter your ID: ")

age = 18
has_id = True

if age >= 18 and has_id:
    print("You can enter")

else:
    print("You cannot enter")

# Exercise 2 OR 

cash = input("Do your have cash: ")
card = input("Do you have card: ")

cash = True
card = False

if cash or card:
    print("You can pay")
else:
    print("You can not pay")

# Exercise 3 NOT

input("is_raining: ")

is_raining = True

if not is_raining:
    print("Take an umbrella")
else:
    print("You can go outside")


# LESSON 6 CHALLENGE 
# Create a Student Admission Checker

print("===== STUDENT ADMISSION =====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your score" ))

("===== RESULT =====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Score: {score}")


if age >= 18 and score >= 60:
    print("Admission approved")
else:
    print("Admission denied")

# Driving Eligibility Checker


name = input("Enter your name: ")
age = int(input("Enter your age: "))
has_license = True

print("===== DRIVING ELIGIBILITY =====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Has_license: {True}")

if age >= 18 or has_license:
    print("You are eligible to drive")
else:
    print("You are not eligible to drive")
