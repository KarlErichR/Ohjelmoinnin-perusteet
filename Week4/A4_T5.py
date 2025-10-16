print("Prograam starting.\n")

start = int(input("Insert starting point: "))
endd = int(input("Insert stopping point: "))
ins = int(input("Insert inspection point: "))

while True:
    if start >= endd:
        print("\nStarting point value must be less than the stopping point value")
        if ins < start or ins > endd:
             print("Inspection value must be within the range of start and stop.")
             break
    if ins < start or ins > endd:
        print("\nInspection value must be within the range of start and stop.")
        break
    print("\nFirst loop - inspection with breake:")
    for i in range(start, endd):
         if i == ins:
            break
         else:
             if i != ins-1:
                 print(i, end=" ")
             else:
                 print(i)
    print("\nSecond loop - inspection with continue:")
    for i in range(start, endd):
         if i == ins:
               continue
         else:
            if i == endd-1:
                print(i)
            else:
                print(i, end=" ")
    break

print("\nProgram ending.")