input = float(input("Enter your age: "))
if input <= 1:
    print("You are an infant.")
elif input < 13:
    print("You are an child.")
elif input < 20:
    print("You are an teenager.")
else:
    print("You are an adult.")