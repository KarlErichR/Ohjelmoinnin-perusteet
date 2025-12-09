from A8_T1LIB import activatePause

def askUser() -> str:
    return input("Your choice: ")

def showOption():
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")
    return None

def chooseActivity():
    duration = 0
    while True:
        showOption()
        choice = int(askUser())
        match choice:
            case 1:
                duration = int(input("Insert pause duration (s): "))
                print()
            case 2:
                activatePause(duration)
            case 0:
                print("Exiting program.\n")
                break
    return None

def main():
    print("Program starting.")
    chooseActivity()
    print("\nProgram ending.")
    return None

if __name__ == "__main__":
    main()