import numpy as np
def prime(n):
    """
    Find Prime CF of two numbers using (sieve of eratosthenes Alogrithm)
    """
    p=np.arange(n)
    p[0]=0
    p[1]=0
    for i in range (2,n):
        p[i]=1

    for i in range (2,n):
        if p[i]==1:
            j=2                            
        while(i*j<n):
            p[i*j]=0
            j+=1

    print("Twin prime numbers till {}".format(n))
    for i in range (n-1):
        if p[i]==1 and p[i+2]==1:
            print(i,i+2)

prime(1000)
        
