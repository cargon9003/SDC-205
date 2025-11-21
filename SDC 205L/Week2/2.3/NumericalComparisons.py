# 2.3 Code Challenge - Numerical Comparisons
# Student ID: cargon9003

from datetime import date

# First line: student ID and today's date
print("cargon9003", date.today())

# The exact list we have to use
numbers = [60, 33, 88, 3, 7, 9, 22]

# Second line: print the list
print(numbers)

# Start by assuming the first number is both largest and smallest
largest = numbers[0]
smallest = numbers[0]

# Loop through every number in the list
# 'num' represents the current number we're checking against largest/smallest
for num in numbers:
    if num > largest:
        largest = num          # found a new largest
    if num < smallest:
        smallest = num         # found a new smallest

# Final two lines exactly as required
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")