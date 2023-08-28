import re

def isphonenumber1(phonenumber):
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    return pattern.match(phonenumber) is not None

def isphonenumber(phonenumber):
    if len(phonenumber)!= 12:
        return False
    for i in range(0,3):
        if not phonenumber[i].isdecimal():
            return False
    if phonenumber[3]!='-':
        return False
    for i in range(4,7):
         if not phonenumber[i].isdecimal():
            return False
    if phonenumber[7]!='-':
        return False
    for i in range(8,12):
        if not phonenumber[i].isdecimal():
            return False
    return True

phone_number = input("enter the number in the form \"aaa-bbb-cccc\" ")
if isphonenumber(phone_number):
    print(f"{phone_number} is a valid phone number using without regular expression .")
else:
    print(f"{phone_number} is not a valid phone number without regular expression.")
if isphonenumber1(phone_number):
    print(f"{phone_number} is a valid phone number using regular expression .")
else:
    print(f"{phone_number} is not a valid phone number using regular expression .")