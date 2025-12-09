########################################################
# Task A9_T6
# Developer Karl Erich Remmelgas
# Date 2025-12-09
########################################################
def showOptions() -> None:
    # TODO: Print the menu options
    print("Options:")
    print("1  - Insert line")
    print("2 - Save line")
    print("0 - Exit")
    pass

def askChoice() -> int:
    try:
        choice = int(input("Your choice: "))
        if  (0 <= choice <= 2):
            return choice
        else:
            raise ValueError
    except ValueError:
        pass

def saveLines(PLines: list[str]) -> None:
    filename = input("Insert filename: ")
    with open(filename, "w", encoding = "UTF-8") as f:
        f.writelines(PLines)
    pass

def insertLine(PLines: list[str]) -> None:
    line = input("Insert text: ")
    PLines.append(line)
    pass

def onInterrupt(PLines: list[str]) -> None:
    choice = input("\nSave before quit(y/n)?: ")
    if choice =="y":
        saveLines(PLines)
    else:
         pass

def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")
    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()
            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                saveLines(Lines)
            elif Choice == 0:
                print("Exiting program.")
            else:
                print("Unknown option!")
            print("")
    except KeyboardInterrupt:
        if len(Lines) !=  0:
            onInterrupt(Lines)
        else:
            print()
    Lines.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()

