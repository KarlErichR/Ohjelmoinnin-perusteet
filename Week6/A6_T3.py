def write(sisalto, desfilename):
    print(f"writing content to file '{desfilename}'.")
    with open(str(desfilename), "w") as file:
        file.write(sisalto)
    print("copying operation complete.")
    return None

def read(filename):
    print(f"Reading file '{filename}' content.")
    with open(str(filename), "r") as file:
        sisalto = file.read()
    return sisalto

def main():
    print("Program starting.")
    print("This program can copy a file.")
    filename = input ("Insert source filename: ")
    desfilename = input("Insert desination filename: ")
    sisalto = read(filename)
    print("File content ready in memory.")
    write(sisalto, desfilename)
    print("Program ending.")


if __name__ == "__main__":
    main()