def numberlst():
    numbers = input("Insert comma separated integers: ")
    lst = []
    for i in numbers.split(","):
        i = i.strip()
        try:
            num = int(i)
            lst.append(num)
        except ValueError:
            print(f"Invalid value \'{i}\' detected.")
    if not lst:
        print("No valid integers to analyze.")
        return
    Sum = sum(lst)
    length = len(lst)
    parity = "even" if Sum % 2 == 0 else "odd"
    print(f"There are {length} integers in the list.")
    print(f"Sum of the integers is {Sum} and it's {parity}")
    
def main():
    print("Program starting")
    numberlst()
    print("Program ending.")


if __name__ =="__main__":
    main()