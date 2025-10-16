print("Prograam starting.\n")

start = int(input("Insert starting value: "))
end = int(input("Insert stopping value: "))

print("\nStarting for-loop:")

while start <= end:
    if start < end:
        print(start, end=" ")
        start += 1
    else:
        print(start)
        start += 1
print("\nProgram ending.")