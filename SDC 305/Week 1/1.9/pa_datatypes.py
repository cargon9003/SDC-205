# pa_datatypes.py
# 1.9 Performance Assessment: Data Types & Math Operators
# Student: Carlos | ID: Cargon9003

print("Cargon9003")  # Student ID in output

# Get user input
name = input("Please enter your name: ")
student_id = input("Please enter your Student ID: ")
num1 = int(input("Please enter a whole number: "))
num2 = int(input("Please enter a different second whole number: "))

# Three math calculations (multiplication, division, addition)
result_mult = num1 * num2
result_div = num1 / num2
result_add = num1 + num2

# Output calculations with 2 decimal places
print(f"The result of {num1} times {num2} is: {result_mult:.2f}")
print(f"The result of {num1} divided by {num2} is: {result_div:.2f}")
print(f"The result of {num1} plus {num2} is: {result_add:.2f}")

# Compare numbers
if num1 > num2:
    print("Number 1 is larger than Number 2")
else:
    print("Number 1 is smaller than Number 2")

# Final output: name and ID
print(name)
print(student_id)