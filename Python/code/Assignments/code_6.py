def isArmstrong(s,n):
    if s==n:
        print("{} is Armstrong number".format(n))
    else:
        print("{} is not a Armstrong number".format(n))

def cubesum(n):
    l=[int(x) for x in str(n)]
    s=0
    for ele in l:
        s+=ele**3
    isArmstrong(s,n)

def PrintArmstrong(n):
    cubesum(n)    
 
n=int(input("Enter the number:"))
PrintArmstrong(n)