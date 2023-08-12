#write a python program to find the best of two marks
#out of three test's Marks accepted from the user
#Date:14th June 2023


iMarks1=int(input("enter the first test Marks"))
iMarks2=int(input("enter the second test Marks"))
iMarks3=int(input("enter the third test Marks"))
if iMarks1>iMarks2 :
    if iMarks1>iMarks3 :
        igreatest1=iMarks1
    if iMarks2>iMarks3:
        igreatest2=iMarks2
    else:
        igreatest2=iMarks3

elif iMarks2>iMarks3 :
        igreatest1=iMarks2
        if iMarks1>iMarks3:
            igreatest2=iMarks1
        else:
            igreatest2=iMarks3
else :
    igreatest1=iMarks3
    if iMarks1 > iMarks2:
        igreatest2 = iMarks1
    else:
        igreatest2 = iMarks2

isum=igreatest1+igreatest2
faverage=isum/2
print("Average of the best two test marks is :",faverage)