inputFile = input("enter the valid file name ")

N= int(input("Enter N value "))

filedata=open(inputFile,'r')
linesLists  = filedata.readlines()
print("the following lines are the first ",N," lines of the text file")

for textline in (linesLists[:N]):
    print(textline)




word = input("Enter a word : ")
cnt = 0


for textline in linesLists:
    cnt += textline.count(word)
print("The word ",word," appears", cnt, "times in the file")


filedata.close()