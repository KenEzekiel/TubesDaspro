import B01_cipher
import standard
import readerwriter

# user_data is the user.csv of a save folder
def login(save_folder: str, user_data: list[list[str]]):
    """
    Function for login
    """

    username = input('Enter username: ')
    password = input('Enter password: ')

    user_valid = False

    # Checks if the username is present in database
    # Loop for every line in file user.csv (index 3 on folder save) (ignore the first line)
    for i in range(1, standard.length(user_data)):
        if username == user_data[i][1]:
            user_valid = True
            global user_line_index
            user_line_index = i

    if user_valid:
        if B01_cipher.decrypt(user_data[user_line_index][3]) == password:
            print(f'Welcome to BNMO, {username}!')
            return True
        else:
            print('Username not found or wrong password')
            return False
    else:
        print('Username not found or wrong password')
        return False

"""
user_data = readerwriter.reader("save-file-1", "user.csv")
logged_in = login('save-file-1', user_data)
print(logged_in)
"""