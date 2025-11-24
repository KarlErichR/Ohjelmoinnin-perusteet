def display(list):
    if len(list) !=0:
        print(f"Displaying {len(list)} integers:")
        index = 0
        for i in list:
            ordinal = (index +1)
            print(f"- Index {index} => Ordinal {ordinal} => Integer {i}")
            index += 1
    else:
        print("No integers to display")
    return None


def collect():
    numbers  = []
    while True :
        nm = int(input("Insert positive integer(negative stops): "))
        if nm >= 0:
            numbers.append(nm)
        else:
            break
    return numbers
        

def main():
    print("Program starting.")
    print("Collect positive integers.")
    num = collect()
    print("Stopped collecting positive integers.")
    display(num)
    print("Program ending.")

if __name__ =="__main__":
    main()