import standard
import login
# import readerwriter
# import loader
# still doesn't work, need to debug


# ownership_data is the kepemilikan.csv of a save folder, user_data is the user.csv, while game_data is the game.csv
def search_my_game(ownership_data: list[list[str]], user_data: list[list[str]],game_data: list[list[str]]):
    """
    Procedure that prints user-owned games based on its ID and release year.
    """

    game_id = input('Enter Game ID: ')
    release_year = input('Enter release year: ')

    user_game_id = []  # All Game ID of the currently logged in user

    #  Loop for every entry in kepemilikan.csv excluding the first line
    for i in range(1, standard.length(ownership_data)):

        # if user id in kepemilikan.csv == user id of currently logged in user
        if ownership_data[i][1] == user_data[login.user_line_index][0]:  # should be user_data[login.user_line_index][0]
            user_game_id = standard.append(user_game_id, ownership_data[i][0])  # Append game id

    if standard.length(user_game_id) == 0:
        print('You have no game in your inventory that meets the filters')
    else:
        
        game_data_output = []

        for j in user_game_id:
            #  Loop for every entry in game.csv excluding the first line
            for k in range(1, standard.length(game_data)):

                if j == game_data[k][0]:  # if the game id matches
                    game_data_output = standard.append(game_data_output, game_data[k])
        
        game_data_output_char_length = []

        for L in game_data_output:
            for m in range(5):  # Don't index the stock of game
                char_length_list = []
                char_length_list = standard.append(char_length_list, standard.length(L[m]))
            
            game_data_output_char_length = standard.append(game_data_output_char_length, char_length_list)

        max_char_length = []
        
        for n in range(5):

            max_length = 0
            for o in game_data_output_char_length:
                if o[n] > max_length:
                    max_length = o[n]
            
            max_char_length = standard.append(max_char_length, max_length)
        
        numbered_game_data_output = standard.numbered_list(game_data_output, start=1)

        for p, q in numbered_game_data_output:
            print(f'{p}. {q[0].ljust(max_char_length[0])} | {q[1].ljust(max_char_length[1])} | {q[4].ljust(max_char_length[4])} | {q[2].ljust(max_char_length[2])} | {q[3].ljust(max_char_length[3])}')

# filenames = ["game.csv", "kepemilikan.csv", "riwayat.csv", "user.csv"]
# data = [readerwriter.reader(loader.save_folder, file) for file in filenames]

# search_my_game(data[1], data[3], data[0])