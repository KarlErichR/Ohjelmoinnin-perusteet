########################################################
# Task A9_T3
# Developer Karl Erich Remmelgas
# Date 2025-12-09
########################################################
import sys
def readFile(Pfilename: str, Prows: list[str]):
    try:
        with open(Pfilename, "r", encoding="UTF-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    Prows.append(line)
    except FileNotFoundError:
        print(f"Couln't read file  \"{Pfilename}\".")
        sys.exit(1)
    return None

def display(Pfilename: str, Prows: list[str]):
    print(f"## {Pfilename} ##")
    for line in Prows:
        print(line)
    print(f"## {Pfilename} ##")

def main():
    print("Program starting.")
    rows: list[str] = []
    filename = input("insert filename: ")
    readFile(filename, rows)
    display(filename, rows)
    print("Program ending.")

if __name__ == "__main__":
    main()