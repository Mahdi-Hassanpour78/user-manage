from user import User
from getpass import getpass


def main():
    """The main entry point of the program.
    """
    print("Welcome!\n")
    while True:
        print(">>> MENU <<<")
        print("Press (1) to register new user")
        print("Press (2) to login")
        print("Press (O) to Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            User.register_user()
        elif choice == "2":
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            if username in User.users and User.users[username].login(password):
                print("Login successful!\n")
                while True:
                    print(">>> USER MENU <<<")
                    print("Press (1) view user information")
                    print("Press (2) edit username and phone number")
                    print("Press (3) change password")
                    print("Press(4) logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        print(User.users[username])
                    elif user_choice == "2":
                        User.users[username].change_username()
                        phone_number = input("Enter new phone number: ")
                        User.users[username].phone_number = phone_number
                        print("Username and phone number updated successfully!")
                    elif user_choice == "3":
                        User.users[username].change_password()
                    elif user_choice == "4":
                        break
                    else:
                        print("Invalid choice.Try again.")
            else:
                print("Invalid username or password.Login failed.")
        elif choice.upper() == "O":
            break
        else:
            print("Invalid choice.Try again.")

    print("Good luck")

if __name__ == "__main__":
    main()
