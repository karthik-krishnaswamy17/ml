from code_9 import sumPdivisors

def isPerfect(n):
    r=sumPdivisors(n)
    if r[1]==n :
        print("Yeah! {} is  a perfect number".format(n))
    else:
        print("Sorry! {} is  not a perfect number".format(n))

n=int(input("Enter the number:"))
isPerfect(n)