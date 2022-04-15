import standard


# not to be imported
def index_constructor (game_data : list) :
    """
    Function for generating index for new game automatically
    """
    previous_number = int(game_data[standard.length(game_data)-1][0][4]) * 100 + int(game_data[standard.length(game_data)-1][0][5]) * 10 + int(game_data[standard.length(game_data)-1][0][6])
    new_number = previous_number + 1
    if new_number < 10 :
        new_index = "GAME00" + str(new_number)
    elif new_number < 100 :
        new_index = "GAME0" + str(new_number)
    else :
        new_index = "GAME" + str(new_number)
    return new_index

# not to be imported    
def new_game(game_data : list) :
    """
    Procedure to get input for a new game with validation
    """

    complete = False 
    while complete == False :                       # loop for input completeness validation
        name = str(input("Insert game name: "))
        category = str(input("Insert category: "))
        release_year = str(input("Inset release year: "))
        price = str(input("Insert price: "))
        stock = str(input("Insert beginning stock: "))

        if standard.length(name) == 0 or standard.length(category) == 0 or standard.length(release_year) == 0 or standard.length(price) == 0 or standard.length(stock) == 0 :
            print("Please insert all of the game information to be saved by BNMO.")
        else :
            complete = True

    new_index = index_constructor(game_data)      # generating index for the new game by fetching the latest index from the database + 1
    new_data = [new_index , name, category, release_year, int(price), int(stock)]

    return new_data


def add_game (game_data : list) :
    """
    Procedure to add a new valid game to the inventory
    """
    
    new_data = new_game(game_data)
    game_data = standard.append(game_data, new_data) 
    print("Congratulations! Adding game succeded", new_data[1] + "." )

    return (game_data)


"""
# Example on how to use
print(data[0])
data[0] = add_game(data[0])
print(data[0])

data =[["GAME001","binomo","action","1990",17000,6], ["GAME002","oscta","action","1990",17000,6], ["GAME003","mario","adventure","2022",10000,5]]
data = add_game(data)
print(data)

"""
