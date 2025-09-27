print("Program starting")
print("Insert two integers.")
luku1=int(input("Insert first integer: "))
luku2=int(input("Insert second integer: "))
print("Comparing inserted integers.")
if luku1>luku2:
    print("First integer is greater")
elif luku1<luku2:
    print("Second integer is greater")
else:
    print("Integers are the same")
print()
print("Adding integers together")
summa=luku1+luku2
print(f"{luku1}+{luku2}={summa}\n")
print("Checking the parity of the sum...")
if summa%2==0:
    print("Sum is even")
else:
    print("Sum is odd")
print("Program ending")
