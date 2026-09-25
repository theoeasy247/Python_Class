#Python
age = int(input( "Enter your age"))

if age >= 18:
    print("You are an adult")
else:
    print("You are under age")
    
# Exercise 2- Pass or Fail
# Ask the user for their score

score = int(input("Enter your score"))

if score >= 50:
    print("PASS")
else:
    print("FAIL")

# Exercise3
# Ask the user to enter a number

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")

else:
    print("Odd")

# LESSON 5 CHALLENGE-GRADING SYSTEM
name = input("Enter your name: ")
score = int(input("Enter your score: "))

print("===== STUDENT RESULT =====")
print(f"Name:   {name}")
print(f"Score:  {score}")

if score >= 80:
    print("Grade A")

elif score >= 70:
    print("Grade B")

elif score >= 60:
    print("Grade C")

elif score >= 50:
    print("Grade D")

else:
    print("Grade F")