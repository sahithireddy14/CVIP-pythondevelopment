import random
import string

def generate_random_password(length=12):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets to create the full set of characters to choose from
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a random password by selecting characters from the combined set
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Example usage: generate a random password with a default length of 12 characters
password = generate_random_password()
print(password)
