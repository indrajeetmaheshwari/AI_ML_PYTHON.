import numpy as np


class numpy_analyzer:

    def __init__(self):
        self.arr = None

    # ---------------- CREATE ARRAY ----------------
    def create_array(self):
        print("\nSelect type of array:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number of elements: "))
            elements = list(map(int, input("Enter elements: ").split()))
            self.arr = np.array(elements[:n])

        elif choice == 2:
            row = int(input("Enter number of rows: "))
            column = int(input("Enter number of columns: "))
            elements = list(map(int, input("Enter elements: ").split()))
            self.arr = np.array(elements).reshape(row, column)

        elif choice == 3:
            depth = int(input("Enter depth: "))
            row = int(input("Enter rows: "))
            column = int(input("Enter columns: "))
            elements = list(map(int, input("Enter elements: ").split()))
            self.arr = np.array(elements).reshape(depth, row, column)

        print("\nArray created successfully:")
        print(self.arr)

    # ---------------- INDEXING & SLICING (2D ONLY like images) ----------------
    def slicing(self):
        if self.arr.ndim != 2:
            print("Indexing & slicing shown only for 2D arrays.")
            return

        print("\nChoose operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            row = int(input("Enter row index: "))
            column = int(input("Enter column index: "))
            print("Result:", self.arr[row][column])

        elif choice == 2:
            row1, row2 = map(int, input("Enter row range (start end): ").split())
            column1, column2 = map(int, input("Enter column range (start end): ").split())
            print("\nSliced Array:")
            print(self.arr[row1:row2, column1:column2])

    # ---------------- MATHEMATICAL OPERATIONS ----------------
    def math_operations(self):
        elements = list(map(int, input("Enter same size array elements: ").split()))
        arr2 = np.array(elements).reshape(self.arr.shape)

        print("\nChoose operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Result:\n", self.arr + arr2)
        elif choice == 2:
            print("Result:\n", self.arr - arr2)
        elif choice == 3:
            print("Result:\n", self.arr * arr2)
        elif choice == 4:
            print("Result:\n", self.arr / arr2)

    # ---------------- COMBINE ARRAYS (2D ONLY like images) ----------------
    def combine_arrays(self):
        if self.arr.ndim != 2:
            print("Combine works only for 2D arrays.")
            return

        elements = list(map(int, input("Enter elements of second array: ").split()))
        arr2 = np.array(elements).reshape(-1, self.arr.shape[1])
        combined = np.vstack((self.arr, arr2))
        print("\nCombined Array:")
        print(combined)

    # ---------------- SEARCH / SORT / FILTER ----------------
    def search_and_sort_filter(self):
        print("\nChoose option:")
        print("1. Search value")
        print("2. Sort array")
        print("3. Filter values")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value to search: "))
            print("Found at:", np.where(self.arr == value))

        elif choice == 2:
            print("Sorted Array:")
            print(np.sort(self.arr))

        elif choice == 3:
            value = int(input("Enter minimum value: "))
            print("Filtered Array:")
            print(self.arr[self.arr > value])

    # ---------------- AGGREGATES & STATISTICS ----------------
    def statistics(self):
        print("\nChoose operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Sum:", np.sum(self.arr))
        elif choice == 2:
            print("Mean:", np.mean(self.arr))
        elif choice == 3:
            print("Median:", np.median(self.arr))
        elif choice == 4:
            print("Standard Deviation:", np.std(self.arr))
        elif choice == 5:
            print("Variance:", np.var(self.arr))


# ---------------- MAIN MENU ----------------
def main():
    obj = numpy_analyzer()

    while True:
        print("\nWelcome to the Numpy Analyzer!")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine Arrays")
        print("4. Search, Sort or Filter")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            obj.create_array()
            obj.slicing()

        elif choice == 2:
            obj.math_operations()

        elif choice == 3:
            obj.combine_arrays()

        elif choice == 4:
            obj.search_and_sort_filter()

        elif choice == 5:
            obj.statistics()

        elif choice == 6:
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break


main()