# Exercise 1
print("===== WHILE LOOP =====")
number = 1

while number <= 5:

    print(number)
    number = number + 1

# Exercise 2
print("===== EVEN NUMBERS FROM 2 TO 10 =====")

number = 2

while number <= 10:

    print(number)

    number = number + 2

# Excercise 3
print("===== COUNTDOWN =====")

number = 5

while number >= 1:

    print(number)
# Decrease by 1
    number = number -1

# Exercise 4

print("===== User Input + WHILE LOOP =====")

number = int(input("Enter a number: "))

while number >= 1:

    print(number)

    number = number - 1

# Exercise 5
print("===== FOR LOOP =====")
for number in range(1, 11):
    print(number)

# Exercise 6
print("===== EVEN NUMBER FROM 2 TO 20 =====")

for number in range(2, 21, 2):
    print(number)

# Exercise 7
print("++=== COUNTDOWN ===++")

for number in range(10, 0, -1):
    print(number)

# Exercise 8 use of break

print("++++++++ BREAK ++++++++")

for number in range(1, 10):
    if number == 7:
        break
    print(number)
    
# Exercise 9 Continue

print("@@@@@@@@@@ CONTINUE ~~~~~~~~~~")

for number in range(1, 11):
    if number == 5:
        continue
    print(number)

# Lesson 8 Final Challenge 
print("===== PASSWORD ATTEMPT CHECKER =====")
for attempt in range(1, 4):
    password = input("Enter password: ")

    if password == "python123":
        print("Access, granted") 
        break
    else:
        print("Wrong password")
else:
    print("Access denied")
    