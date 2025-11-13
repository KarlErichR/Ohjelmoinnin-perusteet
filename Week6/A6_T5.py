SEPARATOR = ";"

def Analysing(num):
    print("#### Number analysis - START ####")
    number_list = (num.strip() for numbers in num.split(SEPARATOR))
    print(number_list)
    

def read(fname):
    num = ""
    with open(str(fname), 'r', encoding ='utf-8') as file:
        while True:
            line = file.readline()
            line = line.strip()
            if len(line) ==0:
                break
            else:
                num += line + SEPARATOR
    num = num[:-1]
    return num




def main():
    print("Program starting.")
    import os
    print(os.getcwd())
    filename = input("Insert filename: ").strip()
    numbers = read(filename)
    Analysing(numbers)

if __name__ == "__main__":
    main()