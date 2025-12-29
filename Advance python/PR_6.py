import os

fname = "journal.txt"

while True:
    print("\nWelcome to personal journal manager")
    print("1. add a new entry")
    print("2. view all entries")
    print("3. search for an entry")
    print("4. delete all entries")
    print("5. Exit")

    choice = input("useer input : ")

    # Add Entry
    if choice == "1":
        entry = input("Enter your journal entry:\n")

        file = open(fname, "a")
        file.write(entry + "\n")
        file.close()

        print("Entry added successfully!")

    # View Entries
    elif choice == "2":
        if os.path.exists(fname):
            file = open(fname, "r")
            data = file.read()
            file.close()

            if data == "":
                print("No entries found.")
            else:
                print("\nYour Entries:\n")
                print(data)
        else:
            print("Journal file does not exist.")

    # Search Entry
    elif choice == "3":
        if os.path.exists(fname):
            keyword = input("Enter word related to your entry to search: ")

            file = open(fname, "r")
            found = False

            for line in file:
                if keyword in line:
                    print(line, end="")
                    found = True

            file.close()

            if found == False:
                print("No matching entry found.")
        else:
            print("Journal file does not exist.")

    # Delete All Entries
    elif choice == "4":
        if os.path.exists(fname):
            confirm = input("Are you sure? (yes/no): ")
            if confirm == "yes":
                file = open(fname, "w")
                file.close()
                print("All entries deleted.")
            else:
                print("Delete cancelled.")
        else:
            print("No file found.")

    # Exit
    elif choice == "5":
        print("Thank you for using Journal Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
