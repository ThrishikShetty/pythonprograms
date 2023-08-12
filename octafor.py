def BinToDec(binary):
    binary=str(binary)
    binnum=binary[::-1]
    result=0
    i=0
    for x in str(binnum):
      result = result + int(x) * pow(2, i)
      i=i+1
    return result


def decToHexa(octal):
    octal = oct[2:]
    octal = str(octal)
    octnum = octal[::-1]
    decimal = 0
    i = 0
    for x in str(octnum):
        decimal = decimal+ int(x) * pow(8, i)
        i = i + 1
    hexaDeciNum = ''
    while  decimal!= 0:
        temp = 0
        temp = decimal % 16
        if temp < 10:
            hexaDeciNum = str(temp) + hexaDeciNum
        else:
            hexaDeciNum = chr(temp + 87) + hexaDeciNum
        decimal = decimal // 16
    return hexaDeciNum



bin=input("enter binary number to convert to decimal number ")
binary=bin[2:]
x = {"0", "1"}
y = set(binary)
if y.issubset(x):
    print("decimal value of ", bin, "is", BinToDec(binary))
else:
      print("invalid binary number")

oct=input("enter octal number  to convert to hexadecimal number ")
if oct.find("8")>=0 or oct.find("9")>=0 :
    print("invalid octal number")
else:
    print("hexdeciaml value of ",oct,"is",decToHexa(oct))

