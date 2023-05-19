import hashlib
import uuid
from getpass import getpass


class User:
    """Represents user with username, password, phone number, and ID.

    Returns:
        
    """
    users = {}


    def __init__(self, username: str, password: str, phone_number: str = None):
        """Initializes new instance of the User class.

        Args:
            username (str): username of user
            password (str): password of user
            phone_number (str, optional): phone number of user
        """
        self.username = username
        self.password = User.hash_password(password)
        self.phone_number = phone_number
        self.ID = str(uuid.uuid4())


    @staticmethod
    def hash_password(password: str) -> str:
        """Hashes the provided password using SHA256 algorithm.

        Args:
            password (str): password to bs hashed

        Returns:
            str: hashed password
        """
        return hashlib.sha256(password.encode()).hexdigest()


    @classmethod
    def register_user(cls):
        """Registers a new user by taking the necessary information as input.
        """
        username = input("Enter a username: ")
        while cls.username_exists(username):
            print("Username already exists.\nPlease choose a different username.")
            username = input("Enter username: ")

        password = getpass("Enter password(at least 4 characters): ")
        while len(password) < 4:
            print("Password must be at least 4 characters longs.")
            password = getpass("Enter password(at least 4 characters): ")

        phone_number = input("Optional\nEnter phone number : ")

        user = cls(username, password, phone_number)
        cls.users[user.username] = user
        print("User registered successfully.")


    @classmethod
    def username_exists(cls, username: str) -> bool:
        """Checks if the provided username already exists.

        Args:
            username (str): The username to check.

        Returns:
            bool: True if the username exists, False otherwise.
        """
        return username in cls.users


    def login(self, password: str) -> bool:
        """Validates the provided password for user login.

        Args:
            password (str): The password to validate.

        Returns:
            bool: True if the password is correct, False otherwise.
        """
        hashed_password = User.hash_password(password)
        return self.password == hashed_password


    def change_username(self):
        """Changes the username of the user.
        """
        new_username = input("Enter new username: ")
        while User.username_exists(new_username):
            print("Username already exists.Please choose different username.")
            new_username = input("Enter new username: ")

        self.username = new_username
        print("Username changed successfully.")


    @staticmethod
    def validate_password(password: str) -> bool:
        """Validates the provided password.

        Args:
            password (str): The password to validate.

        Returns:
            bool: True if the password is valid, False otherwise.
        """
        return len(password) >= 4


    def change_password(self):
        """Changes the password of the user.
        """
        current_password = getpass("Enter your current password: ")
        if not self.login(current_password):
            print("Incorrect password.")
            return

        new_password = getpass("Enter new password(at least 4 characters): ")
        new_password_confirm = getpass("Confirm your new password: ")

        if new_password != new_password_confirm:
            print("Passwords don't match.")
            return

        if not User.validate_password(new_password):
            print("Password must be at least 4 characters longs.")
            return

        self.password = User.hash_password(new_password)
        print("Password changed successfully!")


    def __str__(self):
        """Returns a string representation of the user's information.

        Returns:
        """
        return f"Username: {self.username}\nPhone number: {self.phone_number}\nID: {self.ID}"
