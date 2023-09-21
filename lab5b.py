import re


def find_phone_numbers_and_emails(file_path):
        file=open(file_path, 'r') 
        text = file.read()

        phone_pattern = r'\+\d{12}'
        email_pattern = r'\b[A-Za-z0-9]+\@[A-Za-z0-9]+\.[A-Z|a-z]{2,7}\b'

        phone_numbers = re.findall(phone_pattern, text)
        email_addresses = re.findall(email_pattern, text)

        return phone_numbers, email_addresses

file_path = 'newfile.txt'
phone_numbers, email_addresses = find_phone_numbers_and_emails(file_path)
print("Phone Numbers:")
for phone_number in phone_numbers:
    print(phone_number)
print("\nEmail Addresses:")
for email_address in email_addresses:
    print(email_address)
