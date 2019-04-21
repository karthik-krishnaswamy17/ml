def oddNumbers(n):
    if n%2!=0:
        return True

n=int(input("Enter the range:"))
l=range(n)
print("Odd numbers under the range {}:".format(n))
print(list(filter(oddNumbers,l)))
