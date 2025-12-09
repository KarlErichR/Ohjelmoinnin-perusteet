########################################################
# Task A9_T2
# Developer Karl Erich Remmelgas
# Date 2025-12-09
########################################################

import sys

def main():
    print("Program starting.")
    feed = input("Insert exit code(0-255): ")
    code = int(feed)
    if code == 0:
        print("Clean exit")
    else: 
        print("Error code")
    sys.exit(code)
    print("Program ending.")

if __name__ == "__main__":
    main()