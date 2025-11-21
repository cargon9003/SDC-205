# app_menu_flow.py
# 2.4 Project: Application Flow Control
# Student: Carlos Gonzalez
# Student ID: Cargon9003
# Date: November 21, 2025
# Description: Enhanced menu using list + for loop + input validation + error handling

from datetime import datetime

# Application title with Student ID
print("Cargon9003's Spreadsheet Automation Menu")

# Menu options stored in a list (cleaner & scalable)
menu_options = [
    "Input Data",
    "View Current Data",
    "Generate Report"
]

# Display menu using a for loop
print("Choose a number from the following options")
for i in range(len(menu_options)):
    print(f"{i + 1}. {menu_options[i]}")

# Get user input
try:
    choice = int(input("\nEnter your choice: "))
except ValueError:
    choice = -1  # Force invalid if not a number

# Validate choice using if-elif-else
if choice == 1:
    selected = "Input Data"
elif choice == 2:
    selected = "View Current Data"
elif choice == 3:
    selected = "Generate Report"
else:
    selected = None

# Output result
if selected:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"You selected {choice} at {current_time}")
else:
    print("Error: Invalid choice selected.")