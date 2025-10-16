print("Program starting.")

num = int(input("Insert a positive integer: "))
steps= 0
while num != 1:
    print(num, end=" -> ")
    if num % 2 == 0:
        num = num // 2
        steps += 1
    else:
        num = 3 * num + 1
        steps += 1
print(num)
print(f"Sequence had {steps} total steps.")

print("\nProgram ending.")