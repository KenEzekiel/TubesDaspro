import standard
#import readerwriter

# Not to be imported
def function_topup(username: str, balance: int, user_data: list[list[str]]) -> list[list[str]]:  # user_data is the user.csv of a save folder
    """
    Function to top up the balance of a user 
    """

    user_valid = False
    line_index = 0
    
    for i in range(1, standard.length(user_data)):      # Loop for every line in file user.csv (index 3 on folder save) (ignore the first line)

        if username == user_data[i][1]:
            user_valid = True
            line_index = i

    if user_valid:

        current_balance = int(user_data[line_index][5])

        if balance + current_balance < 0:
            print("Input not valid")
        else:
            current_balance += balance
            user_data[line_index][5] = current_balance
            return user_data
            
    else:
        print(f'Username "{username}" not found')


# To be imported
def topup(data: list[list[str]]) -> list[list[str]]:
    """
    Function to get input and inputs it into the function_topup function
    """

    username = input("Input username: ")
    balance = int(input("Input balance: "))
    data = function_topup(username, balance, data)
    return data

"""
# Example on how to use
my_data = readerwriter.reader("save-file-1", "user.csv")
print(my_data)
my_data = topup(my_data)
print(my_data)
"""
