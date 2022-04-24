import standard
import F03_login


# not to be imported
# data is filtered list, index is the location of the targetted attribute, criteria is the previously asked input by search_game_at_store procedure
def filter_str(data : list[list[str]], index : int, criteria : str) -> list[list[str]]:
    """
    Function to create a list filtered by a string attribute
    """

    if criteria == "" :
        temp = data
    else :
        temp = [] # temp is for hosting matching datas

        # traversing to find matching attribute and appending the list to temp
        for i in range(standard.length(data)):
            if criteria == data[i][index] :
                temp = standard.append(temp, data[i])

    return temp 


# not to be imported
def get_max_char_length(filtered_game_data : list[list[str]]) -> list[int]:
    """
    Function to get the maximum character length for each column in the filtered game data (i.e. filtered game.csv according to kepemilikan.csv and user-inputted game_id and release_year)
    """

    filtered_game_data_char_length = []

    for L in filtered_game_data:
        char_length_list = []
        for m in range(5):  # Don't index the stock of game

            # char_length_list is a list of character length for each game entry
            char_length_list = standard.append(char_length_list, standard.length(L[m]))

        # filtered_game_data_char_length is the complete list of list of character length for the filtered game data
        filtered_game_data_char_length = standard.append(filtered_game_data_char_length, char_length_list)


    filtered_game_data_max_char_length = []

    for n in range(5):

        max_length_of_column = 0
        for o in filtered_game_data_char_length:
            if o[n] > max_length_of_column:
                max_length_of_column = o[n]
        
        filtered_game_data_max_char_length = standard.append(filtered_game_data_max_char_length, max_length_of_column) 

    return filtered_game_data_max_char_length   


# ownership_data is the kepemilikan.csv of a save folder, user_data is the user.csv, while game_data is the game.csv
def search_my_game(ownership_data: list[list[str]], user_data: list[list[str]], game_data: list[list[str]]):
    """
    Procedure that prints user-owned games based on its ID and release year.
    """

    game_id = input('Enter Game ID: ').upper()
    release_year = input('Enter release year: ')

    user_game_id = []  # All Game ID of the currently logged in user

    # Loop for every entry in kepemilikan.csv excluding the first line
    for i in range(1, standard.length(ownership_data)):

        # if user id in kepemilikan.csv == user id of currently logged in user, then append the game id of the game with matchin user id
        if ownership_data[i][1] == user_data[F03_login.user_line_index][0]:
            user_game_id = standard.append(user_game_id, ownership_data[i][0])

    if standard.length(user_game_id) == 0:
        print('You have no game in your inventory')
    
    else:
        
        game_data_output = []

        for j in user_game_id:
            # Loop for every entry in game.csv excluding the first line
            for k in range(1, standard.length(game_data)):

                if j == game_data[k][0]:  # if user game id matches game id in game.csv
                    game_data_output = standard.append(game_data_output, game_data[k])

        # Filter based on game_id and release_year
        filtered_game_data_output_by_game_id = filter_str(game_data_output, 0, game_id)
        filtered_game_data_output_by_release_year = filter_str(filtered_game_data_output_by_game_id, 3, release_year)
        filtered_game_data = filtered_game_data_output_by_release_year

        if standard.length(filtered_game_data) == 0:
            print('You have no game in your inventory that pass the filter')
        
        else:
        
            filtered_game_data_max_char_length = get_max_char_length(filtered_game_data)

            print('\nGames in your inventory that meet the filter:')

            for p, q in standard.enum(filtered_game_data, start=1):
                print(f'{p}. {q[0].ljust(filtered_game_data_max_char_length[0])} | {q[1].ljust(filtered_game_data_max_char_length[1])} | {q[4].ljust(filtered_game_data_max_char_length[4])} | {q[2].ljust(filtered_game_data_max_char_length[2])} | {q[3].ljust(filtered_game_data_max_char_length[3])}')
