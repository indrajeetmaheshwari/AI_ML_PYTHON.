# Nested if for Even or Odd Number within a Range
#🔹 Check if a number is even or odd and within a certain range


num = int(input("Enter Number : "))

if num >= 0:
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
else:
    print("The number is negative.")
