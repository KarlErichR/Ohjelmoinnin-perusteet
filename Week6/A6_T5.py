SEPARATOR = ";"

SEPARATOR = ";"

def analyseValues(num):
    number_list = [num.strip() for num in num.split(SEPARATOR)]
    count = len(number_list)
    total = sum(int(n) for n in number_list)
    greatest = max(int(n) for n in number_list)
    average = total / count
    result = (f"Count;Sum;Greatest;Average\n{count};{total};{greatest};{average:.2f}\n")
    return result
    

def readValues(fname):
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
    fname = input("Insert filename: ").strip()
    numbers = readValues(fname)
    print("#### Number analysis - START ####")
    print(f'File "{fname}" results:')
    result = analyseValues(numbers)
    print(result)
    print("#### Number analysis - END ####")
    print("Program ending.")

if __name__ == "__main__":
    main()