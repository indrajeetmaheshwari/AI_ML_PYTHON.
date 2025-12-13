# Age Group Categorization
#🔹 Categorize age into different groups


age=int(input("Enter your Age :"))

if age<=12:
    print("child")
elif age<=19:
    print("teenager")
elif age<=35:
    print("Adult")
elif age<=60:
    print("Middle-aged")
else:
    print("Senior Citizen")
