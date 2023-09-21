num = int(input("Enter a number : "))
temp = num
reverse=0
freq={}
while(num>0):
    digit = num%10
    if(digit in freq) :
        freq[digit]+=1
    else :
        freq[digit]=1
    reverse=(reverse*10)+digit
    num=num//10
if(temp==reverse):
    print("Given number is palindrome")
else:
    print("Given number is not a palindrome")
for key,value in freq.items():
    print("%d : %d"%(key,value))



# val = int(input("Enter a value : "))
# str_val = str(val)
# if str_val == str_val[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# for i in range(10):
#     if str_val.count(str(i)) > 0:
#         print(str(i), "appears", str_val.count(str(i)), "times");
