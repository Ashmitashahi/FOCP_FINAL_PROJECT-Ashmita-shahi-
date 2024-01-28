def del_user():
    """
    Delete a user from the "passwd.txt" file based on the provided username.

    This function prompts the user for a username, reads the contents of the "passwd.txt" file,
    and writes back all lines except the one corresponding to the provided username.

    If the username is found and deleted, it prints "User Deleted."
    If the username is not found, it prints "User not found."
    """
    # Get user input for the username to be deleted
    username = input("Enter username: ").lower()

    # Read all lines from the "passwd.txt" file
    with open("passwd.txt", "r") as file:
        lines = file.readlines()

    # Flag to track if the user is found and deleted
    found = False

    # Open the file in write mode to overwrite its content
    with open("passwd.txt", "w") as file:
        # Iterate through each line in the file
        for line in lines:
            # Check if the line does not start with the specified username
            if not line.startswith(username + ":"):
                # Write the line back to the file
                file.write(line)
            else:
                # Set the found flag to True if the username is found
                found = True

    # Print the appropriate message based on whether the user was found and deleted
    if found:
        print("User Deleted.")
    else:
        print("User not found.")

if __name__ == "__main__":
    # Call the del_user function when the script is executed
    del_user()