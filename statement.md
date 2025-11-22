## Problem Statement

Urban parking spaces are limited, and manual parking management often leads to inefficiency, confusion, and revenue loss. Employees must manually track available slots, note vehicle entry/exit times, calculate fees, and maintain records—tasks that are error-prone and time-consuming.
There is a need for a simple, automated, and reliable system that can:
Track real-time vehicle parking
Automatically calculate parking fees
Maintain a history of completed sessions
Present reports for revenue monitoring
This project solves these issues using a Python-based CLI application that manages parking operations efficiently and accurately.


## Scope of the Project

The scope of this project includes:

Managing parking slots for Cars and Bikes

Recording vehicle entry with timestamps

Maintaining real-time slot occupancy status

Calculating parking duration and fees based on hourly rate

Storing completed parking sessions

Searching for a parked vehicle

Generating revenue and history reports

Menu-based command-line user interface


## Target Users

This system is intended for:

Primary Users

Parking attendants / staff at:

Shopping malls

Residential complexes

Corporate offices

Small commercial parking spaces

Secondary Users

Developers or students learning:

Python basics

CLI design

Data structure-based simulations

Simple modular programming

This project is ideal for educational, demo, or small deployment use cases.


## High-Level Features
The system provides the following major features:

🔹 Parking Slot Management
Initialize dedicated slots for Cars and Bikes

View real-time availability and occupancy


🔹 Vehicle Entry System

Prevent duplicate entries

Assign first available slot

Track entry timestamp

🔹 Vehicle Exit & Billing

Calculate duration based on time difference

Bill using a flat hourly rate

Auto-round up to nearest hour

Vacate slot after exit

🔹 Reporting & History

Generate total revenue summary

Show last 5 completed sessions

Full parking history (via module2)
Vehicle search functionality (via module1)
