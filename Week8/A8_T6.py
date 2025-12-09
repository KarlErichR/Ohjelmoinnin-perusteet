from drawLib import drawCircle, drawSquare, saveSvg, Drawing

def main() -> None:
    # Initialize the drawing object
    Dwg = Drawing()
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        match choice:
            case 1:
                print('Insert-square')
                left = int(askValue1("Left edge position"))
                top = int(askValue1("Top edge position"))
                side = int(askValue1("Side length"))
                fill = askValue1("Fill color")
                stroke = askValue1("Stroke  color") 
                drawSquare(Dwg, left, top, side, fill, stroke)
            case 2:
                print('Insert-circle')
                centerX = int(askValue1("Center X coord"))
                centerY = int(askValue1("Center Y  coord")) 
                radius = int(askValue1("Radius"))
                fill = askValue1("Fill color") 
                stroke = askValue1("Stroke color") 
                drawCircle(Dwg, centerX, centerY, radius, fill, stroke)
            case 3:
                filename = askValue2("Insert filename")
                print(f'Saving file to "{filename}"')
                proceed = input("Proceed (y/n)?: ")
                if proceed == 'y':
                    saveSvg(Dwg, filename)
                    print('Vector saved successfully!')
            case 0:
                print("Exiting program.\n")
                break
        print()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue1(PPrompt: str) -> str:
    return input(f"- {PPrompt}: ")

def askValue2(PPrompt: str) -> str:
    return input(f"{PPrompt}: ")

if __name__ == "__main__":
    main()

