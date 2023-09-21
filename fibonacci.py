 #Defined as a function F as Fn-1 Write a program
def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
num = int(input("Enter a value for Num: "))
if num<=0 :
    print("Error: N must be greater than zero.")
for num in range(1,num+1):
    print (fibonacci(num))


# def fib(iNum):
#     if (iNum == 1):
#         return numlist
#     # elif (iNum == 1):
#     #     numlist.append(1)
#     #     return numlist
#     else:
#         ivalue=2
#         inum1 = 0
#         inum2 = 1
#         numlist.append(1)
#         while(ivalue<inum):
#             numlist.append(inum1+inum2)
#             temp=inum1+inum2
#             inum1=inum2
#             inum2=temp
#             ivalue+=1
#         return numlist

# numlist=[0]
# inum=int(input("enter the number "))
# if(inum>0):
#     print("fibonacii series  is ",fib(inum))
# else:
#     print("invalid input")


