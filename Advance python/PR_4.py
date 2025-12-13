
data = []   



def display_summary():
    if len(data) == 0:
        print("No data available")
        return

    print("\nData Summary:")
    print("Total elements:", len(data))
    print("Minimum value:", min(data))
    print("Maximum value:", max(data))
    print("Sum of values:", sum(data))
    print("Average value:", sum(data) / len(data))



def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)



def filter_data(threshold):
    result = list(filter(lambda x: x >= threshold, data))
    print("Filtered Data (values >= {}):".format(threshold))
    print(result)



def sort_data():
    if len(data) == 0:
        print("No data to sort")
        return

    print("\n1. Ascending")
    print("2. Descending")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Sorted Data (Ascending):")
        print(sorted(data))
    elif choice == 2:
        print("Sorted Data (Descending):")
        print(sorted(data, reverse=True))
    else:
        print("Invalid choice")



def dataset_stats():
    if len(data) == 0:
        print("No data available")
        return

    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)

    print("\nDataset Statistics:")
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Sum:", total)
    print("Average:", average)



while True:
    print("\n--- Data Analyzer and Transformer ---")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        values = input("Enter numbers separated by space: ").split()
        data = []
        for i in values:
            data.append(int(i))
        print("Data stored successfully!")

    elif choice == 2:
        display_summary()

    elif choice == 3:
        num = int(input("Enter number for factorial: "))
        print("Factorial of", num, "is", factorial(num))

    elif choice == 4:
        t = int(input("Enter threshold value: "))
        filter_data(t)

    elif choice == 5:
        sort_data()

    elif choice == 6:
        dataset_stats()

    elif choice == 7:
        print("Thank you for using data analyzer! Program ended.")
        break

    else:
        print("Invalid choice, try again.")