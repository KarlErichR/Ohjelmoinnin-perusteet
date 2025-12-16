########################################################
# Task A10_T5
# Developer Karl Erich Remmelgas
# Date 2025-12-16
########################################################
import sys

def recursiveFactorial(pNum: int) -> int:
    if pNum < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if pNum == 0 or pNum == 1:
        return 1
    return pNum * recursiveFactorial(pNum - 1)

def main() -> None:
  print("Program-starting.")
  raw = input("Insert factorial: ")
  try:
     n = int(raw.strip())
  except ValueError:
    print("Error: please enter an integer.")
    print("Program ending.")
    sys.exit(1)
  print(f"Factorial: {n}!")
  try:
    result = recursiveFactorial(n)
  except ValueError as e:
    print(f"Error: {e}")
    print("Program-ending.")
    sys.exit(1)

  print(f"{n}! = {result}")

  print("Program ending.")

if __name__ == "__main__":
  main()