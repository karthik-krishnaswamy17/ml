from code_7 import prodDigits
n=int(input("Enter the number:"))
c=0
if n<9:
    print("MDR:{} MPersistence:{}".format(n,c))
else:
    while(n>9):
        n=prodDigits(n)
        if n>9:
            c+=1
    print("MDR:{} MPersistence:{}".format(n,c))    
        


