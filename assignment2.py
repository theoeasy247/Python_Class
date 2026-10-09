# Assignment 2:
# Calculate the total cost of three prouducts
# the three products are:

yam = 2000
rice = 1500
oil = 1000
total_cost = yam + rice + oil

print("===== TOTAL COST =====")
print(f"Total_cost: {total_cost}")

# Calculate the average of three numbers

print("~~~~~~~~ AVERAGE ~~~~~~~~~~")
economics = 50
physics = 70
Bible_studies = 85
Average = (economics + physics + Bible_studies)/3
print(f"Average: {Average}")
if Average >= 60:
    print("You have passed")
else:
    print("You have failed")

"""The difference between == and = is that:
== is a comparison operator that checks if two values are equal, while
= is an assignment operator that is used to assign a value to a variable.
"""

# ASSIGNMENT 3STRINGS:
# Ask for user's full name
("========== ASSIGNMENT 3 STRINGS ==========")

full_name = input("Enter your full name: ")

print(f"Full_name: {full_name}")

# printing in uppercase and lowercase
print(full_name.upper())
print(full_name.lower())

full_name = "Iornumbe Saater Theophilus"
full_name.split()
first_name = full_name[0]
last_name = full_name[-1]
print(first_name)
print(last_name)

# create a persoalized f-string message
message = f"i am the one that do this assignment, my name is {full_name}"
print(message)
