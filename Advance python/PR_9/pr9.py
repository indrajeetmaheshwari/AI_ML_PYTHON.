import pandas as pd
import matplotlib.pyplot as plt

df = None   



def load_data():
    global df
    path = input("Enter CSV file path: ")
    try:
        df = pd.read_csv(path)
        print("Dataset loaded successfully")
    except:
        print("Error loading dataset.")



def explore_data():
    if df is None:
        print("Load data first!")
        return

    print("""
            1. Display first 5 rows
            2. Display last 5 rows
            3. Display column names
            4. Display dataset info
        """)
    ch = input("Enter choice: ")

    if ch == "1":
        print(df.head())
    elif ch == "2":
        print(df.tail())
    elif ch == "3":
        print(df.columns)
    elif ch == "4":
        print(df.info())
    else:
        print("Invalid choice")



def handle_missing_data():
    if df is None:
        print("Load data first!")
        return

    print("""
            1. Show missing values
            2. Fill missing values with 0
            3. Drop rows with missing values
        """)
    ch = input("Enter choice: ")

    if ch == "1":
        print(df.isnull().sum())
    elif ch == "2":
        df.fillna(0, inplace=True)
        print("Missing values filled with 0.")
    elif ch == "3":
        df.dropna(inplace=True)
        print("Rows with missing values removed.")
    else:
        print("Invalid choice")



def description():
    if df is None:
        print("Load data first!")
        return
    print(df.describe())


def visualize_data():
    if df is None:
        print("Load data first!")
        return

    print("""
            1. Bar Plot
            2. Line Plot
            3. Scatter Plot
            4. Histogram
            5. Pie Chart
        """)
    ch = input("Enter choice: ")

    try:
        if ch == "1":
            x = input("X column: ")
            y = input("Y column: ")
            plt.bar(df[x], df[y])

        elif ch == "2":
            x = input("X column: ")
            y = input("Y column: ")
            plt.plot(df[x], df[y])

        elif ch == "3":
            x = input("X column: ")
            y = input("Y column: ")
            plt.scatter(df[x], df[y])

        elif ch == "4":
            col = input("Column name: ")
            plt.hist(df[col])

        elif ch == "5":
            col = input("Column name: ")
            df[col].value_counts().plot.pie(autopct="%1.1f%%")

        else:
            print("Invalid choice")
            return

        plt.title("Data Visualization")
        plt.show()

    except:
        print("Error while plotting.")


# -------- Save Visualization --------
def save_plot():
    name = input("Enter file name (example: plot.png): ")
    plt.savefig(name)
    print("Plot saved successfully!")


# -------- Main Menu --------
while True:
    print("""
==== Data Analysis & Visualization Program ====
1. Load Dataset
2. Explore Data
3. Handle Missing Data
4. Generate Descriptive Statistics
5. Data Visualization
6. Save Visualization
7. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        load_data()
    elif choice == "2":
        explore_data()
    elif choice == "3":
        handle_missing_data()
    elif choice == "4":
        description()
    elif choice == "5":
        visualize_data()
    elif choice == "6":
        save_plot()
    elif choice == "7":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice!")
