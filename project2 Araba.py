import random
import string

def generate_password(length, include_special_chars=True):
    """
    Generates a random password.

    Args:
        length (int): The desired length of the password.
        include_special_chars (bool): Whether to include special characters.

    Returns:
        str: The generated password.
    """

    characters = string.ascii_letters + string.digits  
    if include_special_chars:
        characters += string.punctuation 

    if length < 1:
        return "" 

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """
    Main function to interact with the user and generate the password.
    """
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be a positive integer.")
                continue 
            break 
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        include_special = input("Include special characters? (yes/no): ").lower()
        if include_special in ("yes", "y"):
            include_special_chars = True
            break
        elif include_special in ("no", "n"):
            include_special_chars = False
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    password = generate_password(length, include_special_chars)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
