LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DELIMETER = ';'

def readfile(filename)->str:
    content = ""
    with open(filename, "r") as  file:
        row = file.readline()
        while row != "":
            content += row
            row = file.readline()
    return content

def writefile(nextid: int, new_next: int, plainphrase: str):
    encrypted_fname = f"{nextid}_{new_next}.gkg"
    with open(encrypted_fname, "r", encoding= "UTF-8") as e:
        encrypted_content = e.read()

    first_line_encrypted = encrypted_content.split('\n')[0]
    
    plain_content = rot(encrypted_content)
    
    plain_filename = f"{nextid}-{plainphrase}.txt"
    with open(plain_filename, "w", encoding="UTF-8") as f:
        f.write(plain_content)
    
    return first_line_encrypted

def appendfile(currentid: int, nextid: int, passphrase: str):
    new_row = f"{currentid}{DELIMETER}{nextid}{DELIMETER}{passphrase}"
    with open("player_progress.txt", "a", encoding="UTF-8") as f:
        f.write(new_row + "\n")
    print("[Game Progress autosaved!]")

def shiftCharacter(char, alphabet):
    if char in alphabet:
        index = alphabet.index(char)
        new_index = (index + 13) % len(alphabet)
        return alphabet[new_index]
    return char

def rot(safeW):
    result = ""
    for char in safeW:
        if char in LOWER_ALPHABETS:
            result += shiftCharacter(char, LOWER_ALPHABETS)
        elif char in UPPER_ALPHABETS:
            result += shiftCharacter(char, UPPER_ALPHABETS)
        else:
            result += char
    return result

def getLocation(id):
    Location = "Unkown"
    if id == 1:
        Location = "Galba's palace"
    elif id == 2:
        Location = "Otho's palace"
    elif id == 3:
        Location = "Vitellius' palace"
    elif id == 4:
        Location = "Vespasian's palace"
    elif id == 0:
        Location = "Home"
    return Location

# player_progress.txt pitää olla ensimmäinen leveli line 2 : 0;1;qvfpvcyvar
def main():
    print("Travel starting.")
    Playerprogressfile = "player_progress.txt"
    progress = readfile(Playerprogressfile)
    Lastprogress = progress.strip().split("\n")[-1].split(DELIMETER)
    currentLocationid = int(Lastprogress[0])
    currentLocation = getLocation(currentLocationid)
    nextLocationid = int(Lastprogress[1])
    nextLocation = getLocation(nextLocationid)
    password = Lastprogress[2]

    print(f"Currently at {currentLocation}")
    if currentLocationid == nextLocationid:
        print(f"Already at final location: {currentLocation}. No more travel.")
        print("Travel ending.")
        return
    print(f"Traveling to {nextLocation}...")
    print(f"...Arriving to the {nextLocation}.")
    print("Passing the guard at the entrance.")
    PlainPassPhrase = rot(password)
    print(f'"{PlainPassPhrase.upper()}!"')

    print("Looking for the message in the palace...")
    print("Ah, There it is! Seems cryptic.")
    print("Decyphering Emperor's message...")

    next_progress = writefile(currentLocationid, nextLocationid, PlainPassPhrase)
    new_current, new_next, new_passphrase = next_progress.split(DELIMETER)
    new_level = int(new_next) + 1
    new_palace = int(new_current) + 1
    appendfile(int(new_palace), int(new_level), new_passphrase)
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")

    return None

main()