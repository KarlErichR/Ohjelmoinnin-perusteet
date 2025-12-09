########################################################
# Task A9_T1
# Developer Karl Erich Remmelgas
# Date 2025-12-09
########################################################

def collect():
    feed = -1
    Sum = 0
    while feed != 0:
        number = input("insert a floating-point value (0 to stop): ")
        try:
            feed = float(number)
            Sum += feed
        except:
            print(f"Error! \'{number}' couln't be converted to float.")
    return Sum

def main():
    print("Program starting.\n")
    Sum = collect()
    print(f"\nFinal sum is {Sum:.2f}".format(Sum))
    print("Program ending.")


if  __name__ == "__main__":
    main()