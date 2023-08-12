#write a program to  find the similarity between two given strings
#12-07-2023

string1 = input("Enter String 1 ")
string2 = input("Enter String 2 ")

if len(string2) < len(string1):
    shortString = len(string2)
    longString = len(string1)
else:
    shortString = len(string1)
    longString = len(string2)

matchCount = 0
for i in range(shortString):
    if string1[i] == string2[i]:
        matchCount += 1

print("Similarity between two  strings:")
print(matchCount / longString)