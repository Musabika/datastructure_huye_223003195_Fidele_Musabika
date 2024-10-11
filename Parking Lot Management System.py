from collections import deque

parking_slots = [
    {"SlotID": 501, "CarID": "AB1234", "EntryTime": "9:00 AM", "Available": False},
    {"SlotID": 502, "CarID": None, "EntryTime": None, "Available": True},
    {"SlotID": 503, "CarID": None, "EntryTime": None, "Available": True},
    {"SlotID": 504, "CarID": None, "EntryTime": None, "Available": True},
]

parking_stack = []
waiting_queue = deque()

def park_car(car_id, entry_time):
    for slot in parking_slots:
        if slot["Available"]:
            slot["CarID"] = car_id
            slot["EntryTime"] = entry_time
            slot["Available"] = False
            parking_stack.append(slot)  
            print(f"Car {car_id} parked in slot {slot['SlotID']} at {entry_time}.")
            return
    waiting_queue.append({"CarID": car_id, "EntryTime": entry_time})
    print(f"No available parking slots. Car {car_id} added to the waiting queue.")

def remove_car():
    if not parking_stack:
        print("No cars to remove from the parking lot.")
        return
    last_parked_car = parking_stack.pop()
    last_parked_car["CarID"] = None
    last_parked_car["EntryTime"] = None
    last_parked_car["Available"] = True 
    print(f"Car removed from slot {last_parked_car['SlotID']}. Slot is now available.")
    if waiting_queue:
        next_car = waiting_queue.popleft()
        park_car(next_car["CarID"], next_car["EntryTime"])

def show_parking_lot_status():
    print("Parking lot status:")
    for slot in parking_slots:
        status = "Available" if slot["Available"] else f"Occupied by {slot['CarID']} (Entry at {slot['EntryTime']})"
        print(f"Slot {slot['SlotID']}: {status}")

show_parking_lot_status()
park_car("CD5678", "10:00 AM")
park_car("EF9101", "10:30 AM")
remove_car()
park_car("GH2345", "11:00 AM")
show_parking_lot_status()
remove_car()
show_parking_lot_status()
