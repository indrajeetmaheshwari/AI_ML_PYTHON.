'''

#finding greater number fromm give numbers
a=55
b=785
c=12

if a>b:
    if a>c:
        print(a,"is greater")
    else:
        print(c,"is greater")
else:
    if b>c:
        print(b,"is greater")
    else:
        print(c,"is greater")


'''


number = int(input("Enter the number of Fibonacci terms to generate: "))

# Initialize the first two terms
a = 0
b = 1

# Handle edge cases for 0, 1, or 2 terms
if number <= 0:
    print("Please enter a positive integer.")
elif number == 1:
    print("Fibonacci Series:")
    print(a)
else:
    print("Fibonacci Series:")
    print(a)
    print(b)
    # Generate subsequent terms using a loop
    for _ in range(2, number):
        next_term = a + b
        print(next_term)
        a = b
        b = next_term