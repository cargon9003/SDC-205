# spreadsheet_automation_temp.py
# Project: Spreadsheet Automation - Temperature (F to C)
# Student: Carlos | Cargon9003

from datetime import datetime

def convertData(fahrenheit):
    """Converts Fahrenheit to Celsius: (F - 32) * 5/9"""
    return (fahrenheit - 32) * 5 / 9

def getInput():
    entries = int(input("How many entries are you inputting? "))
    print()
    for _ in range(entries):
        date = input("Enter a date (MM/DD/YYYY): ")
        temp_f = float(input("Enter the highest temp for the inputted date (in °F): "))
        
        # Call convertData: passes temp in F, returns temp in C
        temp_c = convertData(temp_f)
        
        print(f"The following was saved at {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]} :")
        print(f"{date},{temp_f},{temp_c:.2f}\n")

def main():
    print("Cargon9003's Spreadsheet Automation Menu")
    print("Choose a number from the following options")
    print("1 Input Data")
    print("2 View Current Data")
    print("3 Generate Report")
    
    choice = input("\n").strip()
    
    if choice == "1":
        print(f"You selected 1 at {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
        getInput()
    else:
        print("Error: The chosen functionality is not implemented yet")

main()