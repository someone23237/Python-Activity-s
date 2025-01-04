name=input("Enter name=")
Sub1=float(input("Enter subject marks 1="))
Sub2=float(input("Enter subject marks 2="))
Sub3=float(input("Enter subject marks 3="))
Sub4=float(input("Enter subject marks 4="))
Sub5=float(input("Enter subject marks 5="))
summarks=Sub1+Sub2+Sub3+Sub4+Sub5
avg=summarks/500
print(f"{name} scored = {summarks}/500")
percent=round((summarks/500)*100)
print(f"{name} scored={percent}%")
if percent>90:
    print("A+")
elif percent>=75 and percent<= 90:
    print("A")
elif percent>+55 and percent<75:
    print("B")
elif percent>+35 and percent<55:
    print("c")
elif percent>+ 20 and percent<35:
    print("you failed D")
else:
    print("you failed F")