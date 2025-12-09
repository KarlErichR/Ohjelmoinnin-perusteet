import hashlib
import os
import time

# Constants
CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"

def ensureFileExists():
    """Ensure credentials file exists with header."""
    # Wait a moment to ensure file handle is released
    time.sleep(0.1)
    
    if not os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "w", encoding="UTF-8") as f:
            f.write("ID;Username;Password\n")
    else:
        # If file exists but is empty, add header
        try:
            with open(CREDENTIALS_FILE, "r", encoding="UTF-8") as f:
                content = f.read()
                if not content or len(content.strip()) == 0:
                    with open(CREDENTIALS_FILE, "w", encoding="UTF-8") as fw:
                        fw.write("ID;Username;Password\n")
        except:
            pass

def findUser(lines: list[str], PUsername: str, PPassword: str):
    for line in lines:
        columns = line.split(DELIMITER)
        if (columns[1] == PUsername and columns[2] == PPassword):
            return True
        else:
            continue
    return False


def newID(lines: list[str]):
    if not lines:
        return 0
    lastID = lines[-1].split(DELIMITER)[0]
    return int(lastID) + 1


def readFile(lines: list[str]):
    """Read credentials from file with retry logic for file locks."""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            time.sleep(0.05 * attempt)  # Small delay on retry
            with open(CREDENTIALS_FILE, "r", encoding="UTF-8") as f:
                next(f)
                for line in f:
                    if line.strip():
                        lines.append(line.strip())
            return None
        except (FileNotFoundError, PermissionError, OSError):
            if attempt == max_retries - 1:
                return None
            time.sleep(0.1)
    return None


def hash_password(password: str) -> str:
    """
    Hash the password using MD5 and return the hex digest.
    """
    # TODO: Implement password hashing
    h = hashlib.md5()
    h.update(password.encode("UTF-8"))
    return h.hexdigest()


def register(PUsername: str, PPassword: str) -> None:
    """
    Register a new user by appending their credentials to the file.
    """
    # TODO: Count existing users to assign a new ID
    ensureFileExists()
    lines: list[str] = []
    readFile(lines)
    id = newID(lines)
    # TODO: Hash the password
    h_pass = hash_password(PPassword)
    # TODO: Write the new user to the file
    max_retries = 3
    for attempt in range(max_retries):
        try:
            time.sleep(0.05 * attempt)
            with open(CREDENTIALS_FILE, "a", encoding="UTF-8") as f:
                f.write(f"{id};{PUsername};{h_pass}\n")
            break
        except (PermissionError, OSError):
            if attempt == max_retries - 1:
                raise
            time.sleep(0.1)


def login(PUsername: str, PPassword: str) -> bool:
    """
    Check if the username and password match an entry in the credentials file.
    """
    lines: list[str] = []
    # TODO: Hash the input password
    h_pass = hash_password(PPassword)
    readFile(lines)
    # TODO: Read the file and compare credentials
    result = findUser(lines, PUsername, h_pass)
    return result


def viewProfile(PUsername: str) -> list[str]:
    """
    Return the user ID and username for the given username.
    """
    # TODO: Read the file and return the matching profile
    lines: list[str] = []
    Result: list[str] = []
    Result.clear()
    readFile(lines)
    for line in lines:
        columns = line.split(DELIMITER)
        if (columns[1] == PUsername):
            Result.append(columns[0])
            Result.append(columns[1])
    return Result


def change_password(PUsername: str, PNewPassword: str) -> None:
    """
    Change the password for the given username.
    """
    # TODO: Read all lines, update the password for the matching user
    lines: list[str] = []
    readFile(lines)
    new_hashed_pass = hash_password(PNewPassword)
    # TODO: Write the updated lines back to the file
    max_retries = 3
    for attempt in range(max_retries):
        try:
            time.sleep(0.05 * attempt)
            with open(CREDENTIALS_FILE, "w", encoding="UTF-8") as f:
                f.write("ID;Username;Password\n")
                for line in lines:
                    columns = line.split(DELIMITER)
                    if columns[1] ==  PUsername:
                        f.write(f"{columns[0]};{columns[1]};{new_hashed_pass}\n")
                    else:
                        f.write(line + "\n")
            break
        except (PermissionError, OSError):
            if attempt == max_retries - 1:
                raise
            time.sleep(0.1)
