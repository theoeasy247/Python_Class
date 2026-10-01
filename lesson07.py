age = 30
has_license = True


if age >= 18: 
    print("You are an adult")
   
    if has_license:
        print("You can drive")
    else:
        print("You need license")
else:
    print("You are too youg to drive")

# Exercise 2
name = input("Enter your name: ")
score = int(input("Enter your score: "))

if score >= 50:
    if score >= 80:
        print("Excellent performance")
    else:
        print("You passed")
else:
    print("You failed")


# LESSON 7 CHALLENGE
# Buld a Bank Withdrawal Checker.

name = input("Enter your name: ")
balance = int(input("Enter your balance: "))
withdrawal_amount = int(input("Enter your amount: "))

if withdrawal_amount > 0:
    if balance >= withdrawal_amount:
        print("Withdrawal successful")
    else:
        print("Insufficient balance")
else:
    print("Invalid withdrawal amount")

