########################################################
# Task A10_T2
# Developer Karl Erich Remmelgas
# Date 2025-12-16
########################################################

import sys

def readvalues(pfilename: str, pvalues:list[int]) -> list[int]:
    try:
        with open(pfilename, "r", encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if line == "":
                    continue 
                try:
                    pvalues.append(int(line))
                except ValueError:
                    print(f"Error: Non-integer value found: '{line}'.")
                    sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File not found: {pfilename}")
        sys.exit(1)
    except OSError as e:
        print(f"Error: Could not open '{pfilename}': {e}")
        sys.exit(1)
    return None


def sumofvalues(pvalues: list[int]) -> int:
    total = 0
    for v in pvalues:
        total += v
    return total


def productofvalues(pvalues: list[int]) -> int:
    product = 1
    for v in pvalues:
        product *= v
    return product


def main() -> None:
    values: list[int] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    readvalues(filename, values)
    s = sumofvalues(values)
    p = productofvalues(values)
    print("# --- Sum of numbers --- #")
    print(s)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(p)
    print("# --- Product of numbers --- #")
    values.clear()
    print("Program-ending.")
    return None


if __name__ == "__main__":
  main()