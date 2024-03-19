import random
import string

def generate_password(length, complexity):
    # Character sets based on complexity
    character_sets = {
        '1': string.ascii_lowercase,
        '2': string.ascii_lowercase + string.ascii_uppercase,
        '3': string.ascii_letters + string.digits,
        '4': string.ascii_letters + string.digits + string.punctuation
    }
    
    # Select the character set based on the user's choice of complexity
    characters = character_sets.get(complexity, string.ascii_lowercase) # Default to simple if invalid complexity
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Prompt the user for the password length
    length = int(input("Enter the desired length of the password: "))
    
    # Prompt the user for the password complexity
    print("Choose the complexity level:")
    print("1: Simple (lowercase letters only)")
    print("2: Medium (lowercase and uppercase letters)")
    print("3: Complex (letters and digits)")
    print("4: Very Complex (letters, digits, and symbols)")
    complexity = input("Your choice (1-4): ")
    
    # Generate the password
    password = generate_password(length, complexity)
    
    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
