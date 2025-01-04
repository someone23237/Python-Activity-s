current=2025
birthyear=int(input("Enter Birthyear"))
age=current-birthyear
print(f"You are {age} years old.")
if age>=18:
    print("You eligible for driving licence")
else:
    print("You are not Eligible for Driving licence")