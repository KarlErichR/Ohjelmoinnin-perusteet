print("Prograam starting.\n")

start = int(input("Insert starting value: "))
end = int(input("Insert stopping value: "))

print("\nStarting for-loop:")

for i in range(start, end+1):
    if i < end:
        print(i , end=" ")
    else:
        print(i)
print("\nProgram ending.")