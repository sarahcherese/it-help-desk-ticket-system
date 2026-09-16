# IT Help Desk Ticket System

A Python-based help desk ticket system that allows users to create, view, update, search, and manage IT support tickets.
## Features

- Create new IT support tickets
- Automatically assign ticket IDs
- View all existing tickets
- Update ticket status
- Search tickets by employee name
- Validate ticket priority and status
- Handle invalid ticket IDs without crashing
- Exit the system through a menu option
## Skills Used

- Python
- Lists
- Dictionaries
- `if` / `elif` statements
- `while` loops
- `for` loops
- Input validation
- `try` / `except` error handling
- Searching and updating stored data
- String methods like `.lower()`
## How to Run

1. Make sure Python is installed on your computer.
2. Clone or download this repository.
3. Open the project folder in Visual Studio Code or another code editor.
4. Run the `help_desk.py` file.
5. Use the numbered menu options to create, view, update, search, or close tickets.
## Sample Output

```
IT HELP DESK
1. Create Ticket
2. View Tickets
3. Update Ticket Status
4. Search Tickets
5. Exit

Choose an option: 1
Enter employee name: Sarah Price
Describe the issue: Laptop will not connect to Wi-Fi
Enter priority (Low, Medium, High): High
Ticket created successfully!

--- TICKET ---
Ticket ID: 1
Employee: Sarah Price
Issue: Laptop will not connect to Wi-Fi
Priority: High
Status: Open
```
## What I Learned

While building this project, I practiced using Python lists and dictionaries, loops, conditional statements, input validation, error handling, and searching and updating stored data. I also learned how to build a menu-driven program and manage multiple records within a Python application.
