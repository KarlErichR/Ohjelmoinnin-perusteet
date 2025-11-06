def read(Filename):
    file = open(str(Filename), "r", encoding="utf-8")
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        print(line, end="")
    file.close()
    return None

def filechoice():
    filename = input("Insert filename: ")
    return filename

def main():
    print("Program starting")
    print("This program can read a file.")
    Filename = filechoice()
    print(f'#### START "{Filename}" ####')
    read(Filename)
    print()
    print(f'#### END "{Filename}" ####')
    print("Program ending")

if __name__ == "__main__":
    main()