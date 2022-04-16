import standard

# not to be imported
# data is filtered list, index is the location of the targetted attribute, criteria is the previously asked input by search_game_at_store procedure
def filter_str (data : list, index : int, criteria : str) -> list:
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
# data is filtered list, index is the location of the targetted attribute, criteria is the previously asked input by search_game_at_store procedure
def filter_int (data : list, index : int, criteria : str) -> list:
    """
    Function to create a list filtered by an integer attribute
    """

    if criteria == "" :
        temp = data
    else :
        temp = [] # temp is for hosting matching datas

        # traversing to find matching attribute and appending the list to temp
        for i in range(standard.length(data)):
            if int(criteria) == data[i][index] :
                temp = standard.append(temp, data[i])

    return temp       

# game_data is game.csv
def search_game_at_store (game_data : list) :
    """
    Procedure to print out a filtered list based on criteria from user input
    """

    id = str(input("Insert game ID: "))
    name = str(input("Insert game name: "))
    category = str(input("Insert category: "))
    release_year = str(input("Inset release year: "))
    price = str(input("Insert price: "))

    # generate a temporary list for hosting data without changing the source
    filtered = ["*" for i in range(standard.length(game_data)-1)]
    for i in range (1, standard.length(game_data)) :                # traversing from 1 to skip data heading
        filtered[i-1] = game_data[i]
    
    # each line creates a new filtered list from the previous filtered list
    filtered = filter_str(filtered, 0, id)
    filtered = filter_str(filtered, 1, name)   
    filtered = filter_str(filtered, 2, category)
    filtered = filter_str(filtered, 3, release_year)
    filtered = filter_int(filtered, 4, price)
    
    print("List of games at store that match the criteria: ")

    if standard.length(filtered) == 0 :
        print("There is no game at store that matches the criteria.")

    else :
        # Generate parsing for non-empty filtered data
        for i in range (standard.length(filtered)): 
            print(str(i+1) + ".", end=" ")

            for j in range (6) :
                print(filtered[i][j], end="")
                character_amount = 0

                for k in range (standard.length(filtered)):
                    if standard.length(str(filtered[k][j])) > character_amount :
                        character_amount = standard.length(str(filtered[k][j]))
                
                print((" " * (character_amount- standard.length(str(filtered[i][j])))), "| ", end="")
            print("")

# Example on how to use 
# data =[["headings"], ["GAME001","binomo","action","3000",17000,6], ["GAME002","oscta","adventure","3001",17300,6], ["GAME003","mario","adventure","1900",10000,5]]
# search_game_at_store(data)