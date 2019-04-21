from code_9 import sumPdivisors
def checkAmicable(n):
    a=dict()
    b=dict()
    for i in range (n):
        o=sumPdivisors(i)[1]
        if o>1 and o!=i:
            a.update({i:o})
            
    # Old Fashion For Loop
    # for k in a.keys():
    #     for k1,v in a.items():
    #         if(k==v and a[v]==k1): 
    #             print(k,a[k])

    # Comprehension list

    c={k:a[k] for k in a.keys() for k1,v in a.items() if (k==v and a[v]==k1)}
    print("Amicable pairs:\n{}".format(c))
 
checkAmicable(int(input("Enter the range to find amicable numbers:")))