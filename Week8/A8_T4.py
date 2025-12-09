import A8_T4LIB as F1

def processChoice(choice: int, timestamps):                   
    match choice:
        case 0:                                             
            print("Exiting program.")                                 
            return False                                         
    
        case 1:                                      
            year = int(input("Insert year: "))                   
            count = F1.calculateYears(year, timestamps)        
            print(f"Amount of timestamps during year '{year}' is {count}\n")              
        case 2:                                      
            month = input("Insert month : ")                           
            count = F1.calculateMonths(month, timestamps)        
            print(f"Amount of timestamps during month '{month}' is {count}\n")
                              
        case 3:                                            
            weekday = (input("Insert weekday: "))
            if not 1 <= weekday <= 7:                         
                print("Invalid weekday. Please enter 1-7.")   
                return True                                  
            count = F1.calculateWeekdays(weekday, timestamps)    
            print(f"Amount of timestamps during weekday '{weekday}' is {count}\n")                                    
    
    return True   

def askChoice() -> int:
    return int(input("Your choice: "))

def showOptions():
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")
    return None                                               

def main():                                                      
    print("Program starting.")                                   

    filename = input("Insert filename: ")          

    timestamps = F1.readTimestamps(filename)                    

    while True:                                                   
        showOptions()                                 

        choice = askChoice()                      

        if not processChoice(choice, timestamps):                 
            break                                                

    print("Program ending.")                                     

if __name__ == "__main__":                                       
    main()                                                       