from collections import deque

available_services = ["Bath", "Haircut", "Nail Clipping", "Ear Cleaning"]
booking_stack = []
appointment_queue = deque()

def book_appointment(customer_name, service):
    if service not in available_services:
        print(f"Service '{service}' is not available.")
        return
    booking = (customer_name, service)
    booking_stack.append(booking)
    appointment_queue.append(booking)
    print(f"Appointment booked: {customer_name} for {service}")

def undo_booking(undo_command):
    undo_command = undo_command.lower().strip()
    if not booking_stack:
        print("No bookings to undo.")
        return
    
    if undo_command == "yes":
        last_booking = booking_stack.pop()
        appointment_queue.remove(last_booking)
        print(f"Booking for {last_booking[0]} ({last_booking[1]}) has been undone.")
    elif undo_command == "no":
        print("Your appointment has been saved.")
    else:
        print("Invalid input! Please try again.")

def process_next_appointment():
    if not appointment_queue:
        print("No appointments to process.")
        return
    next_appointment = appointment_queue.popleft()
    print(f"Processing appointment: {next_appointment[0]} for {next_appointment[1]}")

def show_available_services():
    print("Available services:")
    for service in available_services:
        print(f"- {service}")

show_available_services()
name = input("Your name please? ")
service_request = input("Service to request? ")

book_appointment(name, service_request)
undo_command = input('Do you want to undo the action ("yes" or "no")? ')

undo_booking(undo_command)
book_appointment("Charlie", "Nail Clipping")

process_next_appointment()
process_next_appointment()
