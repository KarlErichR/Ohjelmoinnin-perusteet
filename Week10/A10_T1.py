########################################################
# Task A10_T1
# Developer Karl Erich Remmelgas
# Date 2025-12-16
########################################################
def horizontally(values:list):
  print("# --- Horizontally --- #")
  print(", ".join(values))
  print("# --- Horizontally --- #")



def vertically(values:list):  
  print("# --- Vertically --- #")
  for value in values:
    print(value)
  print("# --- Vertically --- #")


def readFile(filename, values: list):
  with open(filename, "r", encoding="UTF-8") as file:
    for line in file:
        line = line.strip() 
        if line:
            values.append(line)


def main():
  print("Program starting.")
  values = []
  filename = input("Insert filename: ")
  readFile(filename, values)
  vertically(values)
  horizontally(values)
  print("Program ending.")

if __name__ == "__main__":
  main()