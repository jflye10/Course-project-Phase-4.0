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
    user_ids = (filename)
    with open(filename, 'a') as file:
        while True:
            user_id = input("Enter user ID (or 'End' to finish): ")
            if user_id.lower() == "end":
                break
            if user_id in user_ids:
                print("User ID already exists. Try another.")
                continue
            password = input("Enter password: ")
            auth_code = input("Enter authorization code (Admin/User): ")
            if auth_code not in ("Admin", "User"):
                print("Invalid authorization code. Must be 'Admin' or 'User',")
                continue
            file.write(f"{user_id}|{password}|{auth_code}\n")
            user_ids.append(user_id)
            print(f"User added.\n")

def display_users(filename):
    """Display all users from the file."""
    print("\nCurrent Users:")
    try:
        with open(filename, 'r') as file:
            for line in file:
                user_id, password, auth_code = line.strip().split('|')
                print(f"User ID: {user_id}, Password: {password}, Authorization: {auth_code}")
    except FileNotFoundError:
        print("No users found.")

class Login:
    def __init__(self, user_id, password, authorization):
        self.user_id = user_id
        self.password = password
        self.authorization = authorization

def load_users(filename):
    """Load all users as a list of tuples (user_id, password, auth_code)"""
    users = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                users.append(tuple(line.strip().split('|')))
    except FileNotFoundError:
        pass
    return users

def login_process(filename):
    """Authenticate user and control access based on authorization."""
    users = load_users(filename)
    user_dict = {u[0]: (u[1], u[2]) for u in users}

    user_id = input("Enter user ID: ")
    if user_id not in user_dict:
        print("User ID does not exist. Exiting.")
        return

    password = input("Enter password: ")
    if password != user_dict[user_id][0]:
        print("Incorrect password. Exiting.")
        return

    login_obj = Login(user_id, password, user_dict[user_id][1])
    print(f"\nLogged in as: {login_obj.user_id} | {login_obj.password} | {login_obj.authorization}")

    if login_obj.authorization == "Admin":
        print("\nAdmin privileges) You can add new users and view all users.")
        add_new_users(filename)
        display_users(filename)
    else:
        print("\n(User privileges) You can only view users.")
        display_users(filename)

def main():
    filename = "user_date.txt"
    while True:
        print("\n--- User Login System ---")
        print("1. Add New Users")
        print("2. Display Users")
        print("3. Login Process")
        print("4. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            add_new_users(filename)
        elif choice == "2":
            display_users(filename)
        elif choice == "3":
            login_process(filename)
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
            main()