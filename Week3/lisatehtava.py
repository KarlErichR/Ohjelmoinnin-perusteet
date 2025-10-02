#Jos käyttäjätunnus = omanimi ja ikä >=18 ja käyttäjä on admin => avataaan admin sivu
#Jos käyttäjätunnus = omanimi ja ikä >=18 ja käyttäjä ei ole admin => avataan käyttäjä sivu
#Jos ikä <18 => kerrotaan käyttäjälle: ikä ei riitä
#Jos käyttäjätunnus != omanimi => Pääsy kielletty
# admin tunnuksilla valikko: 1.lisää uusi käyttäjä 2.tarkista laitteen toiminta 3. exit
#käyttäjä sivulla valikko: 1. tarkista omat tiedot 2. exit

print("Program starting.")
print("\nTo get to the page follow the instructions.")

name = input("\nInsert your fullname: ")
age = int(input("Insert your age: "))
uname = input("Insert username: ")
admin = input("Are you admin yes/no: ")

if(uname == name and age >= 18 and admin == 'yes'):
    print("\nWelcome to admin page")
    print("\nOptions:")
    print("1 - Add new user")
    print("2 - Check device functionality")
    print("0 - Exit")
    choice = int(input("Your choice: "))
    if(choice == 1):
        print("\nAdding new user...")
    elif(choice == 2):
        print("\nChecking device functionality...")
    elif(choice == 0):
        print("\nExiting...")
    else:
        print("\nUnknown option")
elif(uname == name and age >= 18 and admin == 'no'):
    print("\nWelcome to user page")
    print("\nOptions:")
    print("1 - Check your details")
    print("0 - Exit")
    choice = int(input("Your choice: "))
    if(choice == 1):
        print(f"\nYour details are: \nName: {name} \nAge: {age} \nUsername: {uname} \nAdmin: {admin}")
    elif(choice == 0):
        print("\nExiting...")
    else:
        print("\nUnknown option")
elif(age < 18):
    print("Access denied")
else:
    print("Unkown user")

print("\nProgram ending.")
