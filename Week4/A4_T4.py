print("Program starting.\n")

sanat = []

while True:
    word =  input("Insert word (empty stops): ")
    if word == "":
        break
    else:
        sanat.append(word)
print("\nYou inserted:")
print(f"- {len(sanat)} words")
print(f"- {sum(len(key) for key in sanat)} characters") 

print("\nProgram ending.")