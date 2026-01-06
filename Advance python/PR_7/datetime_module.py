import datetime

def show_datetime():
    print("Current Date & Time:", datetime.datetime.now())

def date_difference():
    firstdate = input("Enter first date (YYYY-MM-DD): ")
    seconddate = input("Enter second date (YYYY-MM-DD): ")

    date1 = datetime.datetime.strptime(firstdate, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(seconddate, "%Y-%m-%d")

    diff = date2 - date1
    print("Difference: ", diff.days, "days")