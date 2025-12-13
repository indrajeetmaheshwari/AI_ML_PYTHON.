# Nested if to Check Range of a Number
#🔹 Check if a number is within a specific range


num = 15

if num >= 10:
    if num <= 20:
        print(f"{num} is between 10 and 20")
    else:
        print(f"{num} is greater than 20")
else:
    print(f"{num} is less than 10")
