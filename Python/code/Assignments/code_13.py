def cubeElements(n):
    return n**3

if __name__ == "__main__":
    n=int(input("Enter the range:"))
    l=range(n)
    o=map(cubeElements,l)
    print("List of cube elements:\n{}".format(list(o)))
    
