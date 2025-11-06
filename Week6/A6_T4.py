DELIMETER = ";"

def read(filename):
    print(f"Reading names from '{filename}'.")
    names = ""
    with open(str(filename), "r") as file:
        while True:
            line = file.readline()
            line = line.strip()
            if len(line) == 0:
                line = file.readline()
                line = line.strip()
                if len(line) == 0:
                    break
                else:
                    names += line + DELIMETER
                    continue
            names += line + DELIMETER
        names = names[:-1]
    print("Analysing names...")
    name_list = [name.strip() for name in names.split(DELIMETER) ]
    print("Analysing complete!")
    return  name_list

def report(list):
    print("#### REPORT BEGIN ####")
    print(f"Name count - {len(list)}")
    print(f"Shortest name - {len(min(list, key=len))} chars")
    print(f"Longest name - {len(max(list, key=len))} chars")
    Sum = sum(len(list) for list in list) / len(list)
    print(f"Avarage name - {Sum:.2f} chars")
    print("#### REPORT END ####")
    return None



def main():
    print("Program  starting.")
    print("This program analyses a list of names from a file.")
    filename = input("Insert filename  to read: ")
    list = read(filename)
    report(list)
    print("Program ending.")

if  __name__ == "__main__":
    main()