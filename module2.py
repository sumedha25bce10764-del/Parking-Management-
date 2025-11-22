from datetime import datetime

def print_full_history(parking_history):
    """Prints the entire parking history."""
    print("\n--- Full Parking History Report ---")
    
    if not parking_history:
        print("The parking history is currently empty.")
        return
        
    print(f"Total Records: {len(parking_history)}")
    print("-" * 80)
    
    # Print each history record in a formatted way
    for i, record in enumerate(parking_history, 1):
        print(f"Record {i}:")
        print(f"  Vehicle: {record['vehicle_num']}")
        print(f"  Slot: {record['slot_id']} ({record['type']})")
        print(f"  Entry: {record['entry_time'].strftime('%Y-%m-%d %H:%M:%S')}")
        if record.get('exit_time'):
            print(f"  Exit: {record['exit_time'].strftime('%Y-%m-%d %H:%M:%S')}")
            # Calculate duration if both times exist
            duration = record['exit_time'] - record['entry_time']
            hours = duration.total_seconds() / 3600
            print(f"  Duration: {hours:.2f} hours")
        print(f"  Amount Paid: ₹{record.get('fee', 0):.2f}")
        print("-" * 40)