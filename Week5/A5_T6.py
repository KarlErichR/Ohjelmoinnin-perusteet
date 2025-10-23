def menu():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def askchoice():
    feed = input("Your choice: ")
    choice = feed.isnumeric()
    if choice:
        return int(feed)
    else:
        return feed

def main():
    print("Program starting.")
    count = 0
    while True:
        menu()
        choice = askchoice()
        if choice == 1:
            print(f"Current count - {count}")
            print()
        elif choice == 2:
            print(f"Count Increased!")
            print()
            count += 1
        elif choice == 3:
            print(f"Cleared count!")
            print()
            count = 0
        elif choice == 0:
            print("Exiting program.")
            print()
            break
        else:
            print("Unknown option!")
            print()
            continue
    print("Program ending.")

main()