########################################################
# Task A9_T7
# Developer Karl Erich Remmelgas
# Date 2025-12-09
########################################################

import sys
import os

def showHelp() -> None:
    print("[Usage] python A9_T7.py src_file dst_file")

def copyFile(srcFile: str, dstFile: str) -> None:
    print(f"Source file \"{srcFile}\"")
    print(f"Destination file \"{dstFile}\"")

    try:
        with open(srcFile, "r") as fsrc:
            data = fsrc.read()

        with open(dstFile, "w") as fdst:
            fdst.write(data)

    except:
        print("File copy failed.")
        sys.exit(-1)

    print("Program ending.")

def main():
    print("Program starting.")
    if len(sys.argv) != 3:
        print("Invalid number of arguments.")
        showHelp()
        sys.exit(1)

    srcFile = sys.argv[1]
    dstFile = sys.argv[2]

    copyFile(srcFile, dstFile)

main()
