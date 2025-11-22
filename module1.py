from datetime import datetime

def search_vehicle_location(parking_slots):
    """Searches for a vehicle's current location by number."""
    print("\n--- Search Vehicle Location ---")
    vehicle_num = input("Enter Vehicle Number to Search: ").strip().upper()
    
    if not vehicle_num:
        print("ERROR: Vehicle number cannot be empty.")
        return
    
    found = False
    for slot in parking_slots:
        if slot['vehicle_num'] == vehicle_num and slot['is_occupied']:
            entry_time_str = slot['entry_time'].strftime('%Y-%m-%d %H:%M:%S')
            print(f"\nFOUND: Vehicle {vehicle_num} is currently parked.")
            print(f"-> Slot ID: {slot['id']} ({slot['type']})")
            print(f"-> Entry Time: {entry_time_str}")
            found = True
            break
            
    if not found:
        print(f"STATUS: Vehicle {vehicle_num} is not currently parked in the lot.")