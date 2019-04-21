def mult(n):
    """
        Function that prints the multiplication table of that number.
    """
    for i in range (1,11):
        print("{0} * {1} ={2}".format(n,i,n*i))

n=int(input("Enter the number:"))
mult(n)