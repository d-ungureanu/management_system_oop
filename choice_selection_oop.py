import management_operations


# Select options function
def select_option():
    while True:
        allowed_options = ["add", "rem", "mod", "id", "list", "size", "exit"]
        selection = input("""
Please choose your desired option:
'add' to add a user
'rem' to remove a user
'mod' to modify a user's details
'id' to display a specific user's details
'list' for the list of all users
'size' for the total number of employees
'exit' to exit the program
 Your choice is: """)
        if selection in allowed_options:
            if selection == "add":
                management_operations.add_employee()
            elif selection == "rem":
                management_operations.remove_employee()
            elif selection == "mod":
                management_operations.update_employee()
            elif selection == "list":
                management_operations.print_employee_db()
            elif selection == "size":
                management_operations.print_employee_db_size()
            elif selection == "id":
                management_operations.print_id_details()
            elif selection == "exit":
                management_operations.save_db_as_json()

                break

        else:
            print("\n _______________________________")
            print("| Please select a valid option. |")
            print(" _______________________________")
