# wtite a program that accepts a sentence and find the number of words , digits , uppercase letters and lower case letters
#12-07-2023
sentence = input("Enter a sentence : ")
wordCount = sentence.split(" ")


digitCount = uppercaseCount = lowercaseCount = 0

for ch in sentence:
    if '0' <= ch <= '9':
        digitCount += 1
    elif 'A' <= ch <= 'Z':
        uppercaseCount += 1
    elif 'a' <= ch <= 'z':
        lowercaseCount += 1
print("This sentence has", len(wordCount), "words")
print("This sentence has", digitCount, "digits");
print("This sentence has", uppercaseCount ,"uppercase letters")
print("This sentence has", lowercaseCount ,"lowercase letters")