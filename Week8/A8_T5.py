from loginLib import login, register, viewProfile, change_password

def main() -> None:
    print("Program starting.")
    mainMenu()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def showUserMenu() -> None:
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")

def mainMenu() -> None:
    while True:
        showOptions()
        choice = askChoice()
        match choice:
            case 1:
                userName = askValue("username")
                passWord = askValue("password")
                if login(userName, passWord) == True:
                    print("Authentication successful!\n")
                    userMenu(userName, passWord)

                else:
                    print("Authentication failed!\n")
                    continue
            case 2:
                userName = askValue("username")
                passWord = askValue("password")
                register(userName, passWord)
                print("User registration completed!\n")
            case 0:
                print("Exiting program.\n")
                break
        pass

def userMenu(PUsername: str, PPassword: str) -> None:
    while True:
        showUserMenu()
        choice = askChoice()
        match choice:
            case 1:
                profile  =  viewProfile(PUsername)
                print(f"Profile ID {profile[0]} - {profile[1]}\n")
            case 2:
                newPass = input("insert new password: ")
                change_password(PUsername, newPass)
                print("Password changed successfully!\n")
            case 0:
                print("Logging out...\n")
                break
        pass

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue(PPrompt: str) -> str:
    return input(f"Insert {PPrompt}: ")

if __name__ == "__main__":
    main()
