LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftCharacter(char, alphabet):
    if char in alphabet:
        index = alphabet.index(char)
        new_index = (index + 13) % len(alphabet)
        return alphabet[new_index]
    return char


def writeFile(full_path, content):
    print("\n#### Ciphered text ####")
    if  full_path == "":
        print("File name not defined.\nAborting save operation.")
        return None
    with open(full_path, "w", encoding="UTF-8") as file:
            file.write(content)
    print("Ciphered text saved!")
    return None



def rot13(words):
    result = ""
    for char in words:
        if char in LOWER_ALPHABETS:
            result += shiftCharacter(char, LOWER_ALPHABETS)
        elif char in UPPER_ALPHABETS:
            result += shiftCharacter(char, UPPER_ALPHABETS)
        else:
            result += char
    return result



def rowcollect():
    print()
    print("Collecting plain text rows for ciphering.")
    words = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        else:
            words.append(row)
    return words

def main():
    print("Program starting.")
    words = rowcollect()
    ciphered_list = [rot13(word) for word in words]
    print("\n#### Ciphered text ####")
    for line in ciphered_list:
        print(line)
    filename = input("Insert filename to save: ")
    writeFile(filename,  ciphered_list)
    print("Program ending.")

if __name__ == "__main__":
    main()
