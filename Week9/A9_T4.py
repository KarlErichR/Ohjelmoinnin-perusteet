########################################################
# Task A9_T4
# Developer Karl Erich Remmelgas
# Date 2025-12-09
########################################################
import sys
TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius():
    feed = input("Insert Celsius: ")
    try:
        Celsius = float(feed)
        if (Celsius < TEMP_MIN) or (Celsius > TEMP_MAX):
            raise Exception(f"{Celsius} temerature out of range.")
    except ValueError:
        print(f"Could not convert string to float: '{feed}'")
        print("Program ending.")
        sys.exit(1)
    return feed

def main():
    print("Program starting.")
    try:
        celsius = collectCelsius()
        print(f"You inserted {celsius} °C")
    except  Exception as err:
        print(err)
    print("Program ending.")

if __name__ == "__main__":
    main()