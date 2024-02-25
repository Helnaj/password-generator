import random
import string


def generate_password(Length, uppercase, Lowercase, numbers, symbols):
    characters=''
    if uppercase:
        characters += string.ascii_uppercase
    if Lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        print("Error,no characters Found.")

    password= ''.join(random.choice (characters) for ln in range (length))
    return password


length = int(input("Enter the Password Length: "))
uppercase = input('Include uppercase yes/no: ').lower() == 'yes'
lowercase = input('Include lowercase yes/no: ').lower() == 'yes'
numbers = input('Include numbers yes/no: ').lower() == 'yes'
symbols = input('Include punctuation yes/no: ').lower() == 'yes'


password = generate_password( length, uppercase, lowercase, numbers, symbols)
print (password)