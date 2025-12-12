# final_capstone_temperature.py
# FINAL PROJECT - Cargon9003
# Full menu + CSV + Excel + Charts + Charts — Temperature (F to C)

import csv
from datetime import datetime
import os
from openpyxl import Workbook
from openpyxl.chart import LineChart, BarChart, Reference

CSV_FILE = r"C:\PythonFiles\TemperatureData.csv"

# === FUNCTION: Save entry to CSV ===
def insertData(data_line):
    """Appends a comma-separated string to the CSV file"""
    try:
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            f.write(data_line + "\n")
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

# === FUNCTION: Convert F to C ===
def convertToCelsius(fahrenheit):
    """Converts Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5 / 9

# === FUNCTION: Input data ===
def getInput():
    try:
        count = int(input("How many entries are you inputting? "))
        if count <= 0:
            print("Please enter a positive number.\n")
            return
    except ValueError:
        print("Invalid input.\n")
        return

    print()
    for _ in range(count):
        date = input("Enter a date (MM/DD/YYYY): ").strip()
        try:
            temp_f = float(input("Enter the highest temp (in °F): "))
        except ValueError:
            print("Invalid temperature. Skipping.\n")
            continue

        temp_c = convertToCelsius(temp_f)
        data_line = f"{date},{temp_f},{temp_c:.2f}"

        if insertData(data_line):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"The following was saved at {now} :")
            print(f"{date},{temp_f},{temp_c:.2f}\n")

# === FUNCTION: View current data ===
def viewData():
    print(f"\nFile: {CSV_FILE}")
    if not os.path.exists(CSV_FILE):
        print("No data recorded yet.\n")
        return

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                print(line.strip())
    print()

# === FUNCTION: Generate Excel + Chart ===
def createChart(csv_path, chart_type="bar"):
    """
    Args:
        csv_path (str): Path to CSV file
        chart_type (str): "bar" or "line"
    Creates final.xlsx with chart using selected data source
    """
    if not os.path.exists(csv_path):
        print("No data to chart.\n")
        return

    # Ask user which column to chart
    print("Which data source:")
    print("1. Original (Fahrenheit)")
    print("2. Converted (Celsius)")
    choice = input("Choose (1 or 2): ").strip()

    use_celsius = choice == "2"

    dates = []
    values = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 3:
                dates.append(row[0])
                val = float(row[2]) if use_celsius else float(row[1])
                values.append(val)

    # Create Excel file
    wb = Workbook()
    ws = wb.active
    ws.title = "Temperature Data"

    # Header
    ws.append(["Date", "Temperature (°F)" if not use_celsius else "Temperature (°C)"])

    # Data
    for d, v in zip(dates, values):
        ws.append([d, v])

    # Create chart
    if chart_type == "line":
        chart = LineChart()
    else:
        chart = BarChart()

    chart.title = f"Cargon9003 {datetime.now().strftime('%m/%d/%Y')}"
    chart.x_axis.title = "Date"
    chart.y_axis.title = "Temperature (°F)" if not use_celsius else "Temperature (°C)"

    data_ref = Reference(ws, min_col=2, min_row=1, max_row=len(dates)+1)
    cats_ref = Reference(ws, min_col=1, min_row=2, max_row=len(dates)+1)

    chart.add_data(data_ref, titles_from_data=True)
    chart.set_categories(cats_ref)

    ws.add_chart(chart, "D2")

    wb.save(r"C:\PythonFiles\final.xlsx")
    print("Excel report created: C:\\PythonFiles\\final.xlsx\n")

# === FUNCTION: Generate report menu ===
def generateReport():
    print("Chart type:")
    print("1. Bar Chart")
    print("2. Line Chart")
    choice = input("Choose (1 or 2): ").strip()
    chart_type = "bar" if choice == "1" else "line"
    createChart(CSV_FILE, chart_type)

# === MAIN MENU ===
def main():
    print("Cargon9003's Spreadsheet Automation Menu")
    print("Choose a number from the following options")
    print("1 Input Data")
    print("2 View Current Data")
    print("3 Generate Report\n")

    choice = input("").strip()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"You selected {choice} at {now}")

    if choice == "1":
        getInput()
    elif choice == "2":
        viewData()
    elif choice == "3":
        generateReport()
    else:
        print("Error: Invalid choice selected.\n")

if __name__ == "__main__":
    main()