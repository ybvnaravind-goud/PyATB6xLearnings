age = int(input("Enter your age\n"))
if(age<=0 or age>100):
    print(f"{age} is not a Valid age")
else:
    if age >= 18:
        print("You are allowed")
    else:
        print("You are not allowed")