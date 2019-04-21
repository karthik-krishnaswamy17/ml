def prodDigits(n):
    l=[int(x) for x in str(n)]
    p=1
    for ele in l:
        p*=ele
    return p    

n=int(input("Enter the number to find products of digits:"))

print("{} is the product of each digits in {}".format(prodDigits(n),n))