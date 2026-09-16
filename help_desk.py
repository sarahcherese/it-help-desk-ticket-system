# Store all help desk tickets
tickets = []
# Main help desk menu
while True:
    print("\nIT HELP DESK")
    print("1. Create Ticket")
    print("2. View Tickets")
    print("3. Update Ticket Status")
    print("4. Search Tickets")
    print("5. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        # create a new ticket
        employee_name = input("Enter employee name: ")
        issue = input("Describe the issue: ")
        priority = input("Enter priority (Low, Medium, High): ")
        while priority.lower() != "low" and priority.lower() != "medium" and priority.lower() != "high":
            print("Error: Priority must be Low, Medium, or High.")
            priority = input("Enter priority (Low, Medium, High): ")
        ticket_id = len(tickets) + 1
        ticket = {
            "id": ticket_id,
            "employee": employee_name,
            "issue": issue,
            "priority": priority,
            "status": "Open"
        }
        tickets.append(ticket)
        print("Ticket created successfully!")
    elif choice == "2":
        # view all tickets
        for ticket in tickets:
            print("\n--- TICKET ---")
            print(f"Employee: {ticket['employee']}")
            print(f"Issue: {ticket['issue']}")
            print(f"Priority: {ticket['priority']}")
            print(f"Status: {ticket['status']}")
            print(f"ID: {ticket['id']}")
    elif choice == "3":
        # update ticket status
        found = False
        try:
            ticket_id = int(input("Enter ticket ID to update: "))
        except ValueError:
            print("Error: Ticket ID must be a number.")
        else:
            for ticket in tickets:
                if ticket["id"] == ticket_id:
                    found = True
                    new_status = input("Enter new status (Open, In Progress, Closed): ")
                    while new_status.lower() != "open" and new_status.lower() != "in progress" and new_status.lower() != "closed":
                        print("Error: Status must be Open, In Progress, or Closed.")
                        new_status = input("Enter new status (Open, In Progress, Closed): ")
                    ticket["status"] = new_status
                    print("Ticket status updated successfully!")
                    break
        if not found and "ticket_id" in locals():
            print("Error: Ticket ID not found.")
    elif choice == "4":
        # Search tickets by employee name
        search_name = input("Enter employee name to search: ")
        found = False
        for ticket in tickets:
            if ticket["employee"].lower() == search_name.lower():
                found = True
                print("\n--- TICKET ---")
                print(f"Ticket ID: {ticket['id']}")
                print(f"Employee: {ticket['employee']}")
                print(f"Issue: {ticket['issue']}")
                print(f"Priority: {ticket['priority']}")
                print(f"Status: {ticket['status']}")
        if found == False:
            print("Error: Employee name not found.")
    elif choice == "5":
        print("Exiting Help Desk System...")
        break