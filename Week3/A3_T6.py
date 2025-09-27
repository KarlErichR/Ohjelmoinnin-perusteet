print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")

print("\nOptions:")
print("1 - Lenght")
print("2 - Weight")
print("0 - Exit")
choice1 = input("Your choice: ")
if choice1 == "1":
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    choice2 = input("Your choice: ")
    if choice2 == "1":
        meter = float(input("Insert meters: "))
        km = meter / 1000
        print(f"{meter} m is {round(km, 1)} km")
    elif choice2 == "2":
        km = float(input("Insert kilometers: "))
        meter = km * 1000
        print(f"{km} km is {round(meter, 1)} m")
    elif choice2 == "0":
        print("Exiting...")
        print("\nProgram ending.")
    else:
        print("Unknown option.")
        print("\nProgram ending.")
elif choice1 == "2":
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    choice2 = input("Your choice: ")
    if choice2 == "1":
        gr = float(input("Insert grams: "))
        lb = gr / 453.6
        print(f"{gr} g is {round(lb, 1)} lb")
    elif choice2 == "2":
        lb = float(input("Insert pounds: "))
        gr = lb * 453.6
        print(f"{lb} lb is {round(gr, 1)} g")
    elif choice2 == "0":
        print("Exiting...")
        print("\nProgram ending.")
    else:
        print("Unknown option.")
        print("\nProgram ending.")
elif choice1 == "0":
    print("Exiting...")
    print("\nProgram ending.")
else:
    print("Unknown option.")
    print("\nProgram ending.")