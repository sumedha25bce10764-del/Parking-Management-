# Parking Lot Management Sysyem
## Project Overview
This project is a command-line based Parking Lot Management System built using Python.
It allows users to efficiently manage car and bike parking, track vehicle entry and exit, calculate parking fees, and generate revenue reports. The system maintains live slot status and stores completed parking sessions for reporting and analysis.
The application uses a simple in-memory data structure (lists of dictionaries) to simulate the parking lot, making it easy to understand and extend.

## Features

🔹 Slot Management
Initialize parking lot with 10 car slots and 5 bike slots
Display real-time slot availability
Separate status view for Cars and Bikes

🔹 Vehicle Entry
Assigns the first available slot based on vehicle type
Prevents duplicate entries of the same vehicle
Automatically timestamps the entry time

🔹 Vehicle Exit
Calculates parking duration
Rounds billing time up to the nearest hour (minimum 1 hour)
Computes parking fee based on a universal hourly rate
Records completed parking sessions in history

🔹 Revenue & Reporting
View total accumulated revenue
Display last 5 completed parking sessions
Full parking history view (via module2)
Search for a vehicle’s slot location (via module1)

🔹 Additional Functionalities
Clean, menu-driven CLI interface
Easy to expand with more modules (modular design)

## Technologies / Tools Used

Python 3.x, 

datetime module, 

Custom Modules (module1, module2), 

Basic Data Structures (Lists, Dicts)

## How to Install & Run the Project

1️⃣ Prerequisites
Make sure you have:
Python 3.8+
A terminal/command prompt
Check Python version:
python --version

2️⃣ Project Setup
Create a project folder:
mkdir parking_system
cd parking_system
Place the following files inside:
main.py (your provided script)
module1.py
module2.py
Make sure both modules contain the required functions:
module1.search_vehicle_location()
module2.print_full_history()

3️⃣ Run the Application
python main.py
You will see a menu like:
=== Parking System Menu ===
1. Display Slot Status
2. Park Vehicle
3. Exit Vehicle & Pay
4. Generate Revenue Report
5. Search Vehicle Location
6. Print Full Parking History
7. Exit Program

## Instructions for Testing

Here is a step-by-step flow to test all features:

🚗 1. Test Vehicle Entry

Choose option 2

Enter vehicle number (e.g., KA01AB1234)

Enter type: Car or Bike

Repeat with additional vehicles until a type fills up.

📋 2. View Slot Status

Choose option 1

Verify slot allocation visually

🔍 3. Search Vehicle Location

Choose option 5

Enter a parked vehicle number

Should show the slot ID

🚙 4. Exit a Vehicle

Choose option 3

Enter the same vehicle number

System will:

✔ Calculate duration

✔ Calculate fee

✔ Vacate the slot

📊 5. Revenue Report

Choose option 4

Shows:

Total revenue

Last 5 completed sessions

📜 6. Full History

Choose option 6

Shows all completed parking sessions in tabular format

❌ 7. Exit Application

Choose 7
