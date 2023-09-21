
def isPrime(n):
    if(n==1 or n==0):
	    return False
    for i in range(2,n):
	    if(n%i==0):
	        return False
    return True




l =int(input("enter the lower bound"));
u =int(input("enter the upper bound"));

for i in range(l,u+1):
    if(isPrime(i)):
    	print(i,end=" ")
