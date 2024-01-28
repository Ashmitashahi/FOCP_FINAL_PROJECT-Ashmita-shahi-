import getpass
import codecs

def user_exists(username):
    """
    Check if the given username already exists in the "passwd.txt" file.

    Parameters:
    - username (str): The username to check.

    Returns:
    - bool: True if the username exists, False otherwise.
    """
    with open("passwd.txt", "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if parts[0] == username:
                return True
    return False

def login():
    """
    Prompt the user for a username and password to authenticate.

    The function checks if the entered username exists in the "passwd.txt" file.
    If the username exists, it compares the entered password with the stored encoded password.
    If the credentials match, it prints "Access granted," otherwise, it prints "Access denied."
    If the username is not found, it prints "Access denied. User not found."
    """
    # Get user input for the username
    username = input("User: ").lower()

    # Check if the entered username exists
    if not user_exists(username):
        print("Access denied. User not found.")
        return

    # Get user input for the password
    password = getpass.getpass("Password: ")
    
    # Check if the entered password matches the stored encoded password
    with open("passwd.txt", "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if parts[0] == username and codecs.encode(password, 'rot_13') == parts[2]:
                print("Access granted.")
                return

    # Print "Access denied" if the username is found but the password is incorrect
    print("Access denied.")

if __name__ == "__main__":
    # Call the login function when the script is executed
    login()