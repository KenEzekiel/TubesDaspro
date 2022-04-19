import standard

def change_game (game_data : list):
    """
    Procedure to change game information from game data matrix
    """

    id = str(input("Insert game ID: "))

    # finding matching game ID in game data matrix
    found = False
    i = 1
    while (found == False) and (i < standard.length(game_data)):      # Loop for every line in file game.csv (index 3 on folder save) (ignore the first line)
        if  id == game_data[i][0]:
            line_index = i
            found = True
        else :
            i += 1

    if found == False :
        print("There's no game with that ID!")

    else :      # ID is found
        name = str(input("Insert game name: "))
        if name != "" :
            game_data[line_index][1] = name
        category = str(input("Insert category: "))
        if category != "" :
            game_data[line_index][2] = category
        release_year = str(input("Insert release year: "))
        if release_year != "" :
            game_data[line_index][3] = release_year
        price = str(input("Insert price: "))
        if price != "" :
            game_data[line_index][4] = int(price)
        return game_data

"""
# Example on how to use
data =[["Heading"], ["GAME001","binomo","action","1990",17000,6], ["GAME002","oscta","action","1990",17000,6], ["GAME003","mario","adventure","2022",10000,5]]
data = change_game(data)
print(data)
"""
