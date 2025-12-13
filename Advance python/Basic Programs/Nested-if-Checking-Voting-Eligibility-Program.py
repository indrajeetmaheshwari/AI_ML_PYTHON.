# Nested if for Voting Eligibility
#🔹 Check age and citizenship for voting eligibility


age = 18
citizenship = "USA"

if age >= 18:
    if citizenship == "USA":
        print("You are eligible to vote.")
    else:
        print("You are not a citizen.")
else:
    print("You are underage and cannot vote.")
