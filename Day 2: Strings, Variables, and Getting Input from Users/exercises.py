# 1. Ask the user for their name and age, assign theses values to two variables, and then print them.
name = input("Please enter your name: ")
age = input("Please enter your age: ")
print("Your name is " + name + " and you are " + age + " years old.")

# 2. Investigate what happens when you try to assign a value to a variable that you’ve already defined. Try printing the variable before and after you reuse the name.
var = 1
print(var)
var = 2
print(var)

# 3. Below you’ll find some code with a number of errors. Try to go through the program line by line and fix the issues in the code. I’d encourage you to try running the program while you’re working on it, as reading the error messages is great practice for debugging your own programs.
hourly_wage = input("Please enter your hourly wage: ")

print("Hourly wage: ")
print(hourly_wage)

hours_worked = input("How many hours did you work this week? ")

print("Hours worked: ")
print(hours_worked)