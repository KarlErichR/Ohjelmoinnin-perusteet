########################################################
# Task A10_T3
# Developer Karl Erich Remmelgas
# Date 2025-12-09
########################################################

import sys
from A10_TLib import readValues, displayValues, bubbleSort

def main() -> None:
    # Initialize
    Values: list[int] = []
    Filename = ""

    print("Program starting.")
    if len(sys.argv) == 2:
        Filename = sys.argv[1]
    else:
        Filename = input("Insert filename: ")
    readValues(Filename, Values)
    displayValues(Filename, Values, "Raw")
    bubbleSort(Values, PAsc=True)
    displayValues(Filename, Values, "Ascending")
    bubbleSort(Values, PAsc=False)
    displayValues(Filename, Values, "Descending")
    Values.clear()
    print("Program ending.")


if __name__ == "__main__":
    main()
