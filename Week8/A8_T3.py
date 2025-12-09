from A8_T3LIB import Summ, average 

def readFile(filename , Pfile: list[float]):
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            line = line.strip()
            if line:
                Pfile.append(float(line))
    return None


def askChoice() -> int:
    return int(input("Your choice: "))

def showOptions():
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")
    return None

def main():
    print("Program starting.")
    values: list[float] = []
    while True:
        showOptions()
        choice = askChoice()
        match choice:
            case 1:
                filename = input("Insert filename: ")
                readFile(filename, values)
                print()
            case 2:
                print(f"Amount of values - {len(values)}\n")
            case 3:
                print(f"Sum of values - {Summ(values)}\n")
            case 4:
                print(f"Average of values  - {average(values)}\n")
            case 0:
                print("Exiting program.\n")
                break
    print("Program ending.")


if __name__ == "__main__":
    main()