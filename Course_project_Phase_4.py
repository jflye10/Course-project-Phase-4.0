# Joshua Flye, CIS 261, Course Project Phase 4.0

def load_users_ids(filename):
    """Load existing user IDs from the data file into a list."""
    user_ids = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                user_id = line.strip().split('|')[0]
                user_ids.append(user_id)
    except FileNotFoundError:
        pass
    return user_ids

def add_new_users(filename):
    """Prompt for user data, validate, and append to the file."""
    user_ids = load_user_ids(filename)
    with open(filename, 'a') as file:
        while True:
            user_id = input("Enter user ID (or 'End' to finish): ")
            if user_id.lower() == "end":
                break
            if user_id in user_ids:
                print("User ID already exists. Try another.")
                continue
            password = input("Enter password: ")
            auth_code not in ("Enter authorization code (Admin/User): "):
            if auth_code not in ("Admin", "User"):
                print("Invalid authorization code. Must be 'Admin' or 'User',")
                continue
            file.write(f"{user_id}|{password}|{auth_code}\n")
            user_ids.append(user_id)
            print("User added.\n")

def display_users(filename):
    """Display all users from the file."""
    print("\nCurrent Users:")
    try:
        with open(filename, 'r') as file:
            for line in file:
                user_id, password, auth_code = line.strip().split('|')
                