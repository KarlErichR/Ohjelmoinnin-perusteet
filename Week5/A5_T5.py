

def menu():
  print("Options:")
  print("1 - Insert word")
  print("2 - Show current word")
  print("3 - Show current word in reverse")
  print("0 - Exit")
  return None

def askchoice():
    feed = input("Your choice: ")
    return int(feed)

def askword():
    feed = input("Insert word: ")
    print()
    return feed

def main():
    print("Program starting.")
    word=""
    while True:
     menu()
     choice = askchoice()
     if choice == 1: 
         word = askword()
     elif choice == 2:
            print(f"Current word - '{word}'\n")
     elif choice == 3:
            print(f"Word reversed - '{word[::-1]}'\n")
     elif choice == 0:
            print("Exiting program.")
            break
     else:
            print("Unkown option.\n")
    print()
    print("Program ending.")
    
main()