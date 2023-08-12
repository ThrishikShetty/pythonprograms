#Defined as a function F as Fn-1 Write a program
def fib(iNum):
    if (iNum == 1):
        return numlist
    # elif (iNum == 1):
    #     numlist.append(1)
    #     return numlist
    else:
        ivalue=2
        inum1 = 0
        inum2 = 1
        numlist.append(1)
        while(ivalue<inum):
            numlist.append(inum1+inum2)
            temp=inum1+inum2
            inum1=inum2
            inum2=temp
            ivalue+=1
        return numlist

numlist=[0]
inum=int(input("enter the number "))
if(inum>0):
    print("fibonacii series  is ",fib(inum))
else:
    print("invalid input")


