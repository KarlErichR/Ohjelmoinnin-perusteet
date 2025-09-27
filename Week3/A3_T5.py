print("Program starting.\n")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
choice = input("Your choice: ")
if choice == "1":
    cels = float(input("Insert the amount of Celsius: "))
    fahr = (float(cels) * 1.8) + 32
    print(f"{cels}°C equals to {round(fahr, 1)}°F")
elif choice == "2":
    fahr = float(input("Insert the amount of Fahrenheit: "))
    cels = (float(fahr) - 32) / 1.8
    print(f"{fahr}°F equals to {round(cels, 1)}°C")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.") 