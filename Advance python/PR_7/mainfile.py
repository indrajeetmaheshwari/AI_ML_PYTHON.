from datetime_module import show_datetime, date_difference
from math_module import factorial, compound_interest
from random_module import random_number, random_password
from uuid_module import generate_uuid
from file_module import create_file, write_file, read_file
from explore_module import explore

while True:
    print("\n==== Multi Utility Toolkit ====")
    print("1. Date & Time")
    print("2. Math Operations")
    print("3. Random Data")
    print("4. UUID")
    print("5. File Operations")
    print("6. Explore Module")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_datetime()
        date_difference()

    elif choice == "2":
        factorial()
        compound_interest()

    elif choice == "3":
        random_number()
        random_password()

    elif choice == "4":
        generate_uuid()

    elif choice == "5":
        create_file()
        write_file()
        read_file()

    elif choice == "6":
        explore()

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
