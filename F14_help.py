import role_validator

def help(user: str, save_folder: str):
    """
    Procedure to print the instructions for the main program
    """

    is_user_admin = role_validator.is_admin(user, save_folder)
    if is_user_admin:
        print("========== HELP ==========")
        print("")
        print("1. register - Register a new user")
        print("2. login - Log in to the program")
        print("3. add_game - Adding a game to the database")
        print("4. change_game - Changing a game in the database")
        print("5. change_stock - Changing the stock of a game in the database")
        print("6. list_available_game - Gives a list of all the available game in the store")
        print("7. search_at_store - Searches the store for a game")
        print("8. topup - Top ups the balance of a user")
        print("9. help - Prints this menu")
        print("10. save - Saves the current working database")
        print("11. exit - Exits the program")
        print("12. magicconch : Hears what the great magic conch has to say")
        print("13. tictactoe : Play TicTacToe")
    else:
        print("========== HELP ==========")
        print("")
        print("before logging in:")
        print("1. login - Log in to the program")
        print("2. help - prints this menu")
        print("")
        print("after logging in:")
        print("1. list_available_game - Gives a list of all the available game in the store")
        print("2. buy_game - Buys a game with the current balance")
        print("3. list_my_game - Lists owned games")
        print("4. search_my_game - Searches owned games")
        print("5. search_at_store - Searches the store for a game")
        print("6. history - Prints the transaction history")
        print("7. help - Prints this menu")
        print("8. save - Saves the current working database")
        print("9. exit - Exits the program")
        print("10. magicconch : Hears what the great magic conch has to say")
        print("11. tictactoe : Play TicTacToe")
