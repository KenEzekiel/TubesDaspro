import standard

def change_stock(game_data : list) :
    """
    Procedure to change the amount of stock of an existing game, complete with input validation
    """
    id = input("Insert game ID: ")

    # finding matching game ID in game data matrix
    found = False
    i = 1
    while found == False and i < standard.length(game_data):      # Loop for every line in file game.csv (index 3 on folder save) (ignore the first line)
        if  id == game_data[i][0]:
            line_index = i
            found = True
        else :
            i += 1

    if found == False :
        print("There's no game with that ID!")

    else :    # ID is found
        added_stock = int(input("Insert amount: "))

        if game_data[line_index][5] + added_stock < 0 :
            print(game_data[line_index][1], "stock substraction failed due to not enough stock. Current stock:", game_data[line_index][5], "(<", "(abs(added_stock))" + ")" )
        else :
            game_data[line_index][5] += added_stock
            if added_stock == 0 :
                print("No changes were made to the amount of", game_data[line_index][1] + "'s stock. Current stock:", game_data[line_index][5])
            elif added_stock > 0 :
                print(game_data[line_index][1], "stock addition succeeded. Current stock:", game_data[line_index][5])
            else :      # added_stock < 0
                print(game_data[line_index][1], "stock substraction succeeded. Current stock:", game_data[line_index][5])
            return game_data
                
"""
# Example on how to use
data =[["Heading"], ["GAME001","binomo","action","1990",17000,6], ["GAME002","oscta","action","1990",17000,6], ["GAME003","mario","adventure","2022",10000,5]]
data = change_stock(data)
print(data)
"""