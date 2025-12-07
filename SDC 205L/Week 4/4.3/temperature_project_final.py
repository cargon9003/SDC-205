# temperature_project_final.py
# FINAL CAPSTONE PROJECT - Cargon9003
# Full menu, CSV save/load, real data persistence, professional look

import csv
from datetime import datetime
import os

# File path for persistent storage
CSV_FILE = r"C:\PythonFiles\TemperatureData.csv"

# === FUNCTION: Save a single entry to CSV (append or create) ===
def insertData(filepath, data_string):
    """Appends a comma-separated string to the CSV file. Creates file if it doesn't exist."""
    try:
        with open(filepath, "a", newline="") as f:
            f.write(data_string + "\n")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

# === FUNCTION: Read and display all data from CSV ===
def viewData(filepath):
    """Reads and prints all entries from the CSV file with full path shown."""
    print(f"\nThe file {filepath}")
    
    if not os.path.exists(filepath):
        print("No data has been recorded yet.\n")
        return
    
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
            if not lines:
                print("No data has been recorded yet.\n")
            else:
                for line in lines:
                    print(line.strip())
        print()
    except Exception as e:
        print(f"Error reading file: {e}\n")

# === FUNCTION: Convert Fahrenheit to Celsius ===
def convertToCelsius(fahrenheit):
    """Converts Fahrenheit temperature to Celsius"""
    return (fahrenheit - 32) * 5/9

# === FUNCTION: Input multiple temperature entries ===
def getInput():
    try:
        count = int(input("How many entries are you inputting? "))
        if count <= 0:
            print("Please enter a positive number.\n")
            return
    except ValueError:
        print("Invalid number entered.\n")
        return

    print()
    for _ in range(count):
        date = input("Enter a date (MM/DD/YYYY): ").strip()
        try:
            temp_f = float(input("Enter the highest temp for the inputted date (in °F): "))
        except ValueError:
            print("Invalid temperature. Skipping entry.\n")
            continue

        temp_c = convertToCelsius(temp_f)
        data_line = f"{date},{temp_f},{temp_c:.2f}"

        if insertData(CSV_FILE, data_line):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            print(f"The following was saved at {now} :")
            print(f"{date},{temp_f},{temp_c:.2f}\n")

# === MAIN MENU ===
def main():
    print("Cargon9003's Spreadsheet Automation Menu")
    print("Choose a number from the following options")
    print("1 Input Data")
    print("2 View Current Data")
    print("3 Generate Report\n")

    choice = input("").strip()

    print(f"You selected {choice} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")

    if choice == "1":
        getInput()
    elif choice == "2":
        viewData(CSV_FILE)
    elif choice == "3":
        print("Report generation coming in final version!\n")
    else:
        print("Error: Invalid choice selected.\n")

# Start the program
if __name__ == "__main__":
    main()