print("Program starting.")
fahr = input("Insert fahrenheits: ")
cels = (float(fahr) - 32) / 1.8
print(f"{fahr}°F is {round(cels, 1)}°C")

print("Program ending.")