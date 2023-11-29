import random
import string

def generate_password(length=12):
    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure at least one character from each set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password with random characters
    password.extend(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the password to make it more random
    random.shuffle(password)

    # Convert the list of characters to a string
    password = ''.join(password)

    return password

def generate_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

if _name_ == "_main_":
    # User input for the length and number of passwords
    password_length = int(input("Enter the length of the passwords: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))

    # Generate passwords
    passwords = generate_passwords(num_passwords, password_length)

    # Print the generated passwords
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")