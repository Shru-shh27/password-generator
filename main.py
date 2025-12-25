import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!#$%&()*+@^"
all_chars = lowercase + uppercase + digits + symbols

print("Welcome to Password Generator!")
length = int(input("Enter password length: "))

if length < 8:
    print("Error: Password must be at least 8 characters long.")

else:
    password = []

    password += random.choice(lowercase)
    password += random.choice(uppercase)
    password += random.choice(digits)
    password += random.choice(symbols)

    for _ in range(length):
        password += random.choice(all_chars)

    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)
   
print("Your password is : ",password)