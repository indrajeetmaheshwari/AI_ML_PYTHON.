#  Nested if with Multiple Conditions
#🔹 Check if a student passed based on multiple subject marks



maths=int(input("Enter your Maths Marks : "))
english=int(input("Enter your English Marks : "))
science=int(input("Enter your Science Marks : "))

if maths >=50:
    if english>=50:
        if science>=50:
            print("You are Passed in all subjects !!")
        else:
            print("you are fail in science.")
    else:
        print("you are fail in english .")
else:
    print("you are fail in maths .")
