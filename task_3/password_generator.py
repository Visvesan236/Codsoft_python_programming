import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")
    
    # Define the character sets to use
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Ensure the password has at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the rest of the password length with random choices from all sets
    all_characters = uppercase + lowercase + digits + special_characters
    password += random.choices(all_characters, k=length-4)
    
    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)
    
    # Convert the list to a string and return it
    return ''.join(password)

# Example usage
password = generate_password(12)
print("Generated Password:", password)
