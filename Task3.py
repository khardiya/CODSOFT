import random
import string

def generate_password(length):
    # Define the characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    while True:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        
        # Generate the password
        password = generate_password(length)
        
        # Display the password
        print(f"Generated Password: {password}")
        
        # Ask the user if they want to generate another password
        choice = input("Do you want to generate another password? (yes/no): ").strip().lower()
        
        if choice != 'yes':
            print("Exiting the password generator. Goodbye!")
            break

main()
