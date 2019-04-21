import math 
def primefactors(n):
    c=0
    for i in range (2,int(math.sqrt(n))+1):
            while (n%i==0):
                n=n/i
                c+=1
                print(i)
    if c==0 :
        print("{} is a prime number.No prime factors for prime number.".format(n))

i=int(input("Enter any number to find prime factors:"))
primefactors(i)
