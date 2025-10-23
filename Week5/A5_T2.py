def frameword(PWord):
    print("*"* (len(PWord)+4))
    print(f"* {PWord} *")
    print("*"* (len(PWord)+4))
    return None

def main():
    print("Program starting.")
    Word = input("Insert word: ")
    print()
    frameword(Word)
    print()
    print("Program ending.")
    return None


main() 