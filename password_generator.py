import random
import string
def generate_password(length):
    if length < 4:
        return "Password length should be at least 4"

    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    
    all_chars = letters + digits + symbols
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_chars, k=length - 3)

   
    random.shuffle(password)
    return ''.join(password)


try:
    length = int(input("Enter the password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
