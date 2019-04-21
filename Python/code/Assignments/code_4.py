def fact(num):
    """
    Old School method to find factorial of a number without using recursive.
    """
    if num==0 or num==1:
        return 1
    else:
        p=1
        for i in range (2,num+1):
            p*=i
        return p    
            
def permutation(n,r):
    result=fact(n)/fact(n-r)
    print("Permutation of p({0},{1})={2}".format(n,r,result))

def combination(n,r):
    result=fact(n)/(fact(r)*fact(n-r))
    print("Combination of p({0},{1})={2}".format(n,r,result))

n=int(input("Enter number of Objects:"))
r=int(input("Enter the time of objects taken at time: "))
combination(n,r)
permutation(n,r)