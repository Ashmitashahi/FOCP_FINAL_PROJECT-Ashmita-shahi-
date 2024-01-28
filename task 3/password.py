import getpass
import codecs

def user_exists(username, lines):
    """
    Check if the given username already exists in the provided list of lines.

    Parameters:
    - username (str): The username to check.
    - lines (list): List of lines from a file.

    Returns:
    - bool: True if the username exists, False otherwise.
    """
    for line in lines:
        parts = line.strip().split(":")
        if parts[0] == username:
            return True
    return False

def passwd():
    """
    Change the password for a user in the "passwd.txt" file.

    The function prompts the user for a username and the current password.
    If the username is found and the current password is correct, it allows the user to
    enter a new password and confirms it before updating the "passwd.txt" file.
    If the new password and confirmation match, it updates the file and prints "Password changed."
    If the new password and confirmation do not match, it prints "Passwords do not match. Password not changed."
    If the username is not found or the current password is incorrect, it prints "User not found or incorrect password."
    """
    # Get user input for the username
    username = input("User: ").lower()

    # Get user input for the current password
    current_password = getpass.getpass("Current Password: ")

    # Read all lines from the "passwd.txt" file
    with open("passwd.txt", "r") as file:
        lines = file.readlines()

    # Check if the entered username exists and the current password is correct
    if not user_exists(username, lines):
        print("User not found or incorrect password.")
        return

    # Flag to track if the user is found and updated
    found = False

    # Open the file in write mode to overwrite its content
    with open("passwd.txt", "w") as file:
        # Iterate through each line in the file
        for line in lines:
            parts = line.strip().split(":")

            # Check if the line corresponds to the entered username and current password
            if parts[0] == username and codecs.encode(current_password, 'rot_13') == parts[2]:
                # Get user input for the new password and confirmation
                new_password = getpass.getpass("New Password: ")
                confirm_password = getpass.getpass("Confirm: ")
                encrypted_passwd = codecs.encode(confirm_password, "rot_13")

                # Check if the new password and confirmation match
                if new_password == confirm_password:
                    # Write the updated line to the file
                    file.write(f"{parts[0]}:{parts[1]}:{encrypted_passwd}\n")
                    found = True
                    print("Password changed.")
                else:
                    # Print a message if the new password and confirmation do not match
                    print("Passwords do not match. Password not changed.")
            else:
                # Write the unchanged line back to the file
                file.write(line)

    # Print appropriate messages based on whether the user was found and updated
    if not found:
        print("User not found or incorrect password.")

if __name__ == "__main__":
    # Call the passwd function when the script is executed
    passwd()