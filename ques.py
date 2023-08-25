class Process:
    def __init__(self, process_id, process_name, start_time, priority):
        self.process_id = process_id
        self.process_name = process_name
        self.start_time = start_time
        self.priority = priority

    def __str__(self):
        return f"P_ID: {self.process_id.ljust(6)} Process: {self.process_name.ljust(20)} Start Time: {str(self.start_time).ljust(10)} Priority: {self.priority}"

# Sample data
processes = [
    Process("P1", "VSCode", 100, "MID"),
    Process("P23", "Eclipse", 234, "MID"),
    Process("P93", "Chrome", 189, "High"),
    Process("P42", "JDK", 9, "High"),
    Process("P9", "CMD", 7, "High"),
    Process("P87", "NotePad", 23, "Low"),
    # Add more processes here
]

# Function to sort and print processes based on user input
def sort_and_print_processes(processes, sort_key):
    if sort_key == 1:
        sorted_processes = sorted(processes, key=lambda x: x.process_id)
    elif sort_key == 2:
        sorted_processes = sorted(processes, key=lambda x: x.start_time)
    elif sort_key == 3:
        sorted_processes = sorted(processes, key=lambda x: x.priority)
    else:
        print("Invalid sort key.")
        return

    for process in sorted_processes:
        print(process)

# Main loop
while True:
    print("Select sorting criteria:")
    print("1. Sort by Process ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")
    print("4. Exit")
    
    user_input = input()
    
    if user_input == "4":
        print("Exiting the program.")
        break
    
    try:
        user_input = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid option.")
        continue

    if user_input >= 1 and user_input <= 3:
        sort_and_print_processes(processes, user_input)
    else:
        print("Invalid option. Please enter a valid option.")
