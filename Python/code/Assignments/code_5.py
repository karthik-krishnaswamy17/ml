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

print(dec2bin(16))





