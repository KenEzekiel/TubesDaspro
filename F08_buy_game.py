# F08 - Membeli Game

# Masalah:
# Ada NoneType error?

import standard

# Functions below are heavily inspired by module F11
# "For whoever made it, thank you!" ~Sri Prana

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

        # traversing to find unmatching attribute and appending the list to temp
        for i in range(standard.length(data)):
            if criteria != data[i][index] :
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

        # traversing to find exceeding attribute and appending the list to temp
        for i in range(standard.length(data)):
            if int(criteria) >= data[i][index] :
                temp = standard.append(temp, data[i])

    return temp

# game_data is game.csv
# my_game still has unspecified excel file
def buy_game(money, game_data : list, my_game: list) :
    """
    Procedure to print out a filtered list based on criteria from user input
    """

    id = str(input("Masukkan ID Game: "))
    price = money
    stock = 0
    
    filtered1 = ["*" for i in range(standard.length(game_data)-1)]
    for i in range (1, standard.length(game_data)) :                # traversing from 1 to skip data heading
        filtered1[i-1] = game_data[i]

    filtered2 = ["*" for i in range(standard.length(my_game)-1)]
    for i in range (1, standard.length(my_game)) :                # traversing from 1 to skip data heading
        filtered2[i-1] = my_game[i]

    # each line creates a new filtered list from the previous filtered list
    filtered1 = filter_str(filtered1, 0, id)
    filtered2 = filter_str(filtered2, 0, id)
    filtered1 = filter_int(filtered1, 5, stock)
    filtered1 = filter_int(filtered1, 4, price)

    if standard.length(filtered1) == 0 :
        print("Tidak ditemukan game dengan ID tersebut")
    else:
        if standard.length(filtered2) >= 0 :
            print("Anda sudah memiliki Game tersebut!")
        else:
            if standard.length(filtered1) == 0 :
                print("Saldo anda tidak cukup untuk membeli Game tersebut!")
            else:
                print("Game dengan ID " + str(id) + " berhasil dibeli!")

# Examples regarding usage
"""
saldo = 100000
data = [["headings"], ["GAME001","BNMO - Play Along With Crypto","Adventure","2022", 100000, 6], ["GAME069","Python Gemink","Programming","1991", 69000, 0], ["GAME666","Hehehe","Comedy","2012", 666000, 5]]
mine = [["headings"], ["GAME001", "BNMO - Play Along With Crypto", "Adventure", "2022", 100000]]
buy_game(saldo, data, mine)
"""
