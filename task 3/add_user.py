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
            existing_username = line.split(":")[0].strip()
            if existing_username == username:
                return True
    return False

def adduser():
    """
    Add a new user to the "passwd.txt" file.

    Returns:
    - bool: True if the user was created successfully, False if the username already exists.
    """
    # Get user input
    username = input("Enter new username: ").lower()
    real_name = input("Enter real name: ")
    passwd = input("Enter password: ")

    # Check if the username already exists
    if user_exists(username):
        print("Cannot add. Most likely username already exists.")
        return False

    # Encrypt the password
    encrypted_passwd = codecs.encode(passwd, "rot_13")

    # Append the user information to the "passwd.txt" file
    with open("passwd.txt", "a") as file:
        file.write(f"{username}:{real_name}:{encrypted_passwd}\n")

    return True

if __name__ == "__main__":
    # Attempt to create a new user
    user_created = adduser()

    # Display appropriate message based on the result
    if user_created:
        print("User Created.")