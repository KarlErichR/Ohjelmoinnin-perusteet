print("Program starting.\n")

print("Check multiplicative persistence.")
num = int(input("Insert an integer: "))
steps = 0


while num !=0:
    if num <10:
        print("No more steps.")
        break
    else:
        digits = [int(i) for i in str(num)]
        num=1
        steps +=1
        for i in range(len(digits)):
            j = digits[i]
            if i != len(digits)-1:
                 print(j, end=" * ")
                 num *= j 
            else:
                num *= j 
                print(f"{j} = {num}")

if num == 0:
    print("No more steps")
    
print(f"\nThis program took {steps} step(s)")

print("\nProgram ending.")
            
            
 