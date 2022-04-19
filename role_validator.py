import readerwriter

def is_admin(username: str, save_folder: str):
    """
    Function to check if the user is an admin or not
    """
    user_data = readerwriter.reader(save_folder, "user.csv")
    line_index = 0
    for i in range(1, len(user_data)):
        if username == user_data[i][1]:
            line_index = i
    user_role = user_data[line_index][4]
    if line_index == 0:
        print("username tidak ada di database")
    if user_role == "Admin":
        return True
    else:
        return False

#print(is_admin("kenezekiel", "save-file-1"))