import standard

# not to be imported
def temporary_data (game_data : list) :
    """
    Function to generate temporary list for hosting data without changing the source
    """
    data = ["*" for i in range(standard.length(game_data)-1)]     
    for i in range (1, standard.length(game_data)) :                # traversing from 1 to skip data header
        data[i-1] = game_data[i]
    return data

# not to be imported
def year_ascending(game_data : list) :
    """
    Function to sort data based on release year in ascending order
    """
    sorted = temporary_data(game_data)

    for i in range (standard.length(sorted)-1) :                    # sorting data using selection sort algortihm
        index_min = i

        for j in range (i+1, standard.length(sorted)):
            if int(sorted[index_min][3]) > int(sorted[j][3]) :
                index_min = j

        temp = sorted[index_min]
        sorted[index_min] = sorted[i]
        sorted[i] = temp

    return sorted

# not to be imported
def year_descending(game_data : list) :
    """
    Function to sort data based on release year in descending order
    """
    sorted = temporary_data(game_data)

    for i in range (standard.length(sorted)-1) :                    # sorting data using selection sort algortihm
        index_min = i

        for j in range (i+1, standard.length(sorted)):
            if int(sorted[index_min][3]) < int(sorted[j][3]) :
                index_min = j

        temp = sorted[index_min]
        sorted[index_min] = sorted[i]
        sorted[i] = temp

    return sorted

# not to be imported
def price_ascending(game_data : list) :
    """
    Function to sort data based on price in ascending order
    """
    sorted = temporary_data(game_data)
    
    for i in range (standard.length(sorted)-1) :                    # sorting data using selection sort algortihm
        index_min = i

        for j in range (i+1, standard.length(sorted)):
            if int(sorted[index_min][4]) > int(sorted[j][4]) :
                index_min = j

        temp = sorted[index_min]
        sorted[index_min] = sorted[i]
        sorted[i] = temp

    return sorted

# not to be imported
def price_descending(game_data : list) :
    """
    Function to sort data based on price in ascending order
    """
    sorted = temporary_data(game_data)
    
    for i in range (standard.length(sorted)-1) :                    # sorting data using selection sort algortihm
        index_min = i

        for j in range (i+1, standard.length(sorted)):
            if int(sorted[index_min][4]) < int(sorted[j][4]) :
                index_min = j

        temp = sorted[index_min]
        sorted[index_min] = sorted[i]
        sorted[i] = temp

    return sorted

def sorting (game_data : list) :
    """
    Procedure to print out parsed and sorted game data
    """
    valid = False 

    while valid == False :
        mode = str(input("Sorting mode [year+/year-/price+/price-]: "))

        if mode == "year+" :
            sorted = year_ascending(game_data)
            valid = True
        elif mode == "year-" :
            sorted = year_descending(game_data)
            valid = True
        elif mode == "price+" :
            sorted = price_ascending(game_data)
            valid = True
        elif mode == "price-" :
            sorted = price_descending(game_data)
            valid = True
        elif mode == "" :
            sorted =  temporary_data(game_data)
            valid = True
        else :
            print("Invalid sorting mode. Please try again!")

    # adding header to sorted data
    header = ["ID", "NAME", "CATEGORY", "RELEASE YEAR", "PRICE", "STOCK"]

    temp = ["*" for i in range(standard.length(sorted)+1)]  
    temp[0] = header 
    for i in range (standard.length(sorted)) :
        temp[i + 1] = sorted[i]
    
    sorted = temp

    # Generate parsing for sorted data
    for i in range (standard.length(sorted)): 
        if i == 0 :                         # skip numbering for the header
            print("  ", end= " ")
        else :                              # numbering for the list
            print(str(i) + ".", end=" ")

        for j in range (6) :
            print(sorted[i][j], end="")
            character_amount = 0
            for k in range (standard.length(sorted)):
                if standard.length(str(sorted[k][j])) > character_amount :
                    character_amount = standard.length(str(sorted[k][j]))
            
            print((" " * (character_amount- standard.length(str(sorted[i][j])))), "| ", end="")
        print("")

"""
# Example on how to use
data =[["header"], ["GAME001","binomo","action","3000",17000,6], ["GAME002" ,"oscta","action","3001",17300,6], ["GAME003","mario","adventure","1900",10000,5]]
sorting(data)
"""