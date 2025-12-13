print("Welcome to the Pattern Generator and Number Analyzer!\n")


while True:
    print("Select an Option: ")
    print("1. Generate a Pattern")
    print("2. Analyze a range of Numbers")
    print("3. Exit")
    print("\n")
    choice=int(input("Enter your Choice: "))

    if choice==1:
        row=int(input("Enter the number of rows for the pattern: "))
        print("\nPattern : ")
        for i in range(1, row+1):
            print("*"*i)

    elif choice==2:
        start = int(input("\nEnter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        total = 0
        for num in range(start, end + 1):
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")
            total += num

        print(f"Sum of all numbers from {start} to {end} is: {total}")


    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice.")