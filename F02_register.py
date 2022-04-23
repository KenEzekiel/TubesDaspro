import standard
import B01_cipher


# user_data is the user.csv of a save folder
def register(user_data: list[list[str]]) -> list[list[str]]:
    """
    Function to add a list of id, username, name, ciphered password, role, and balance of user
    to the loaded user.csv data on the main program (GUI.py).
    """

    name = input('Enter name: ')
    username = input('Enter username: ')

    # Loops until the username is valid
    while True:

        try:
            # Username valid characters (-, _, 0-9, A-Z, a-z) validation
            for char in username:
                if not (ord(char) == 45 or ord(char) == 95 or 48 <= ord(char) <= 57 or
                        65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):  # -, _, 0-9, A-Z, a-z respectively
                    print('Username is not valid. Please only use letters, numbers, underscore (_), and dash (-).')
                    raise ValueError

            # Checks if the username is already present
            #  Loop for every entry in user.csv excluding the first line
            for i in range(1, standard.length(user_data)):
                if username == user_data[i][1]:
                    print(f'Username "{username}" already exists, please select a different username.\n')
                    raise ValueError

        except ValueError:
            username = input('Enter username: ')

        else:
            print('Username is available!')
            break

    password = input('Enter password: ')

    id = standard.length(user_data)
    ciphered_password = B01_cipher.encrypt(password)
    role = 'User'  # Register can only add a user, not admin
    balance = 0  # Initial balance is always 0

    new_user = [id, username, name, ciphered_password, role, balance]

    user_data = standard.append(user_data, new_user)

    return user_data

