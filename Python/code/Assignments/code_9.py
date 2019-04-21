def sumPdivisors(n):
    l=[]
    s=0
    if n==1:
        return [[1],1]
    else:    
        for i in range (1,int(n/2)+1):
            if (n%i==0):
                l.append(i)
                s+=i
        return [l,s]
         
if __name__ == "__main__":
    n=int(input("Enter the number:"))
    o=sumPdivisors(n)
    print("Divisor of {} :{}\nSum of these Divisor:{}".format(n,o[0],o[1]))