from code_13 import cubeElements

def evenNumbers(n):
    if n%2==0:
        return True

n=int(input("Enter the range:"))
l=range(1,n)

evenList=list(filter(evenNumbers,l))
cube_of_even_list=list(map(cubeElements,evenList))

print("Cube of even number list:\n{}".format(cube_of_even_list))