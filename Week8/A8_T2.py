from mathLIB import add, substract, multiply, divide

def askChoice() -> int:
    return int(input("Your choice: "))

def showMenu() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Substract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")
    return None

def main():
    print("Program starting.")
    while True:
        showMenu()
        choice = askChoice()
        match choice:
            case 1:
                a = float(input("Insert  first  addend value: "))
                b = float(input("Insert  second  addend value: "))
                result = add(a, b)
                print(f"{a} + {b} = {result}")
            case 2:
                a = float(input("Insert  minuend value: "))
                b = float(input("Insert  subtrahend value: "))
                result = substract(a, b)
                print(f"{a} - {b} = {result}\n")
            case 3:
                a = float(input("Insert  multiplicand value: "))
                b = float(input("Insert  multiplier value: "))
                result = multiply(a, b)
                print(f"{a} + {b} = {result}\n")
            case 4:
                a = float(input("Insert  dividend value: "))
                b = float(input("Insert  divisor value: "))
                result = divide(a, b)
                print(f"{a} + {b} = {result}\n")
            case 0:
                print("Exiting program.")
                break
    print("\nProgram ending.")


if __name__  == "__main__":
    main()