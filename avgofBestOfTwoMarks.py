# write a python program to find the best of two marks
# out of three test's Marks accepted from the user
# Date:14th June 2023


iMarks1=int(input("enter the first test mark"))
iMarks2=int(input("enter the second test mark"))
iMarks3=int(input("enter the third test mark"))
if iMarks1>iMarks2:
    if iMarks2>iMarks3:
        isum=iMarks1+iMarks2
    else:
        isum=iMarks1+iMarks3
else:
    if iMarks1>iMarks3:
        isum=iMarks1+iMarks2
    else:
        isum=iMarks2+iMarks3


faverage=isum/2
print("the best of two test average marks out of three test’s marks",faverage)
