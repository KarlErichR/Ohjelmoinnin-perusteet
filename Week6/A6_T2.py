def write(fname, sname):
    filname = input("Insert filename: ")
    file = open(str(filname), "w")
    file.write(fname + '\n')
    file.write(sname + '\n')
    file.close()
    return None

def Sname():
    feed = input("Insert last name: ")
    return feed

def Fname():
    feed = input("Insert first name: ")
    return feed

def main():
    print("Program starting.")
    fname = Fname()
    sname= Sname()
    write(fname, sname)
    print("Program ending")

if __name__ == "__main__":
    main()