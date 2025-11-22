import time
from datetime import datetime, timedelta
import module1
import module2

# --- Configuration ---
HOURLY_RATE = 50.0  # Flat rate for all vehicle types
CAR_SLOTS = 10
BIKE_SLOTS = 5

# The parking lot state is a simple list of dictionaries for simplicity
# Each slot: {'id': 'C01', 'type': 'Car', 'is_occupied': False, 'vehicle_num': None, 'entry_time': None}
parking_slots = []
parking_history = [] # Stores finished sessions

# --- Core Functions ---

def initialize_parking_lot():
    """Sets up the initial state of the parking lot."""
    for i in range(1, CAR_SLOTS + 1):
        parking_slots.append({
            'id': f'C{i:02d}',
            'type': 'Car',
            'is_occupied': False,
            'vehicle_num': None,
            'entry_time': None
        })
    for i in range(1, BIKE_SLOTS + 1):
        parking_slots.append({
            'id': f'B{i:02d}',
            'type': 'Bike',
            'is_occupied': False,
            'vehicle_num': None,
            'entry_time': None
        })
    print(f"Parking lot initialized with {CAR_SLOTS} Car and {BIKE_SLOTS} Bike slots.")

def display_slot_status():
    """Shows the current status of all slots."""
    print("\n--- Current Slot Status ---")
    car_status = []
    bike_status = []
    
    for slot in parking_slots:
        status = "OCCUPIED" if slot['is_occupied'] else "AVAILABLE"
        info = f"({slot['vehicle_num']})" if slot['vehicle_num'] else ""
        slot_info = f"Slot {slot['id']} ({slot['type']}): {status} {info}"
        
        if slot['type'] == 'Car':
            car_status.append(slot_info)
        else:
            bike_status.append(slot_info)

    print("\nCAR SLOTS:")
    # Display in a readable column format
    for i in range(0, len(car_status), 2):
        print(" | ".join(car_status[i:i+2]))
    
    print("\nBIKE SLOTS:")
    for i in range(0, len(bike_status), 2):
        print(" | ".join(bike_status[i:i+2]))
    print("-----------------------------\n")

def find_available_slot(vehicle_type):
    """Searches for the first available slot of the specified type."""
    for slot in parking_slots:
        if not slot['is_occupied'] and slot['type'] == vehicle_type:
            return slot
    return None

def vehicle_entry():
    """Handles vehicle check-in and slot assignment."""
    print("\n--- Vehicle Entry ---")
    vehicle_num = input("Enter Vehicle Number: ").strip().upper()
    
    # Simple check to see if the vehicle number is already parked
    for slot in parking_slots:
        if slot['vehicle_num'] == vehicle_num:
            print(f"STATUS: Vehicle {vehicle_num} is already parked in slot {slot['id']}.")
            return

    vehicle_type = input("Enter Vehicle Type (Car/Bike): ").strip().capitalize()

    if vehicle_type not in ['Car', 'Bike']:
        print("ERROR: Invalid vehicle type. Must be 'Car' or 'Bike'.")
        return

    available_slot = find_available_slot(vehicle_type)

    if available_slot:
        # Occupy the slot
        available_slot['is_occupied'] = True
        available_slot['vehicle_num'] = vehicle_num
        available_slot['entry_time'] = datetime.now()

        entry_time_str = available_slot['entry_time'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"\nSUCCESS: Vehicle {vehicle_num} parked in slot {available_slot['id']}.")
        print(f"Entry Time: {entry_time_str}")
    else:
        print(f"FAILURE: No available slots for {vehicle_type}.")

def calculate_fee(entry_time, exit_time):
    """Calculates the parking fee based on duration."""
    duration = exit_time - entry_time
    duration_hours = duration.total_seconds() / 3600
    
    # Round up to the nearest hour, minimum 1 hour
    hours_billed = max(1, int(duration_hours) + (1 if duration_hours % 1 > 0 else 0))
    
    total_fee = hours_billed * HOURLY_RATE
    
    duration_str = f"{int(duration.total_seconds() // 3600)}h {int((duration.total_seconds() % 3600) // 60)}m"
    
    return total_fee, duration_str

def vehicle_exit():
    """Handles vehicle check-out, fee calculation, and slot vacating."""
    print("\n--- Vehicle Exit ---")
    vehicle_num = input("Enter Vehicle Number: ").strip().upper()

    session_found = False
    for slot in parking_slots:
        if slot['vehicle_num'] == vehicle_num:
            session_found = True
            
            entry_time = slot['entry_time']
            exit_time = datetime.now()
            
            # 1. Calculate Fee
            total_fee, duration_str = calculate_fee(entry_time, exit_time)
            
            # 2. Record History
            parking_history.append({
                'vehicle_num': vehicle_num,
                'slot_id': slot['id'],
                'type': slot['type'],
                'entry_time': entry_time,
                'exit_time': exit_time,
                'fee': total_fee
            })
            
            # 3. Vacate Slot
            slot['is_occupied'] = False
            slot['vehicle_num'] = None
            slot['entry_time'] = None

            print(f"\nSUCCESS: Vehicle {vehicle_num} exited from slot {slot['id']}.")
            print(f"Parking Duration: {duration_str}")
            print(f"Total Fee: ₹{total_fee:.2f}")
            break

    if not session_found:
        print(f"ERROR: Vehicle {vehicle_num} is not currently parked.")

def generate_revenue_report():
    """Generates a summary of total revenue."""
    print("\n--- Revenue Report ---")
    
    if not parking_history:
        print("No completed parking sessions yet.")
        return

    total_revenue = sum(session['fee'] for session in parking_history)
    
    print(f"Total Revenue Generated: ₹{total_revenue:.2f}")
    
    print("\nRecent Completed Sessions (Last 5):")
    _print_session_list(parking_history[-5:])

def _print_session_list(sessions):
    """Helper function to print session details in a formatted table."""
    print("-------------------------------------------------------------------------")
    print(f"{'Vehicle':<10} | {'Slot':<5} | {'Type':<5} | {'Exit Time':<20} | {'Fee':<10}")
    print("-------------------------------------------------------------------------")
    for session in sessions:
        exit_time_str = session['exit_time'].strftime('%H:%M:%S on %Y-%m-%d')
        print(
            f"{session['vehicle_num']:<10} | {session['slot_id']:<5} | {session['type']:<5} | "
            f"{exit_time_str:<20} | ₹{session['fee']:<9.2f}"
        )
    print("-------------------------------------------------------------------------")

# --- Main Application Loop ---

def main():
    """Runs the main command-line interface."""
    initialize_parking_lot()
    
    while True:
        print("\n=== Parking System Menu ===")
        print("1. Display Slot Status")
        print("2. Park Vehicle")
        print("3. Exit Vehicle & Pay")
        print("4. Generate Revenue Report (Summary)")
        print("5. Search Vehicle Location")  # Module 1
        print("6. Print Full Parking History") # Module 2
        print("7. Exit Program")
        
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            display_slot_status()
        elif choice == '2':
            vehicle_entry()
        elif choice == '3':
            vehicle_exit()
        elif choice == '4':
            generate_revenue_report()
        elif choice == '5':
            module1.search_vehicle_location(parking_slots)  # Pass parking_slots as parameter
        elif choice == '6':
            module2.print_full_history(parking_history)  # Pass parking_history as parameter
        elif choice == '7':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()