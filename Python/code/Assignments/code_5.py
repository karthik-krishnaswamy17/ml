import numpy as np
def dec2bin(n):
    bin=[]
    while (n>0):
        r=int(n%2)
        n=int(n/2)
        bin.append(r)
    bin.reverse()
    
    # Adding the numbers by using power of 10's using one's twos'....
    res = sum(d * 10**i for i, d in enumerate(bin[::-1])) 
    return res
n=int(input("Enter number in decimal format:"))
print("{} in binary:{}".format(n,dec2bin(n)))





