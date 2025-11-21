# pa_decisions_loops.py
# 2.7 Performance Assessment: Decisions, Loops, Processing, Output Formatting
# Student: Carlos (@beastoscarlito)
# Student ID: Cargon9003
# Date: November 18, 2025
# Description: Number guessing game with feedback, try counter, and two loops that increment the correct guess.

print("Cargon9003")

# Get user info
userName = input("What is your name? ")
studentId = input("What is your studentID? ")

print(f"Hello, {userName}! Let's play a guessing game.")

# Secret number (you can change this if you want — I'm using 7)
secretNumber = 7
guess = 0
tries = 0

# Guessing loop with if/else logic
while guess != secretNumber:
    guess = int(input("Please guess a number between 1 and 10 ... "))
    tries += 1
    
    if guess < secretNumber:
        print("You guessed too low")
    elif guess > secretNumber:
        print("You guessed too high")
    else:
        print(f"Congratulations, {userName}! You guessed the number in {tries} tries!")

# WHILE LOOP: Increment correct guess 5 times
print("Output from the 'while' loop:")
increment = 1
counter = 0
while counter < 5:
    print(f"{secretNumber} incremented by {increment} is {secretNumber + increment}")
    increment += 1
    counter += 1

# FOR LOOP: Same thing using for + range
print("Output from the 'for' loop:")
for i in range(1, 6):  # i goes 1 to 5
    print(f"{secretNumber} incremented by {i} is {secretNumber + i}")