import standard

def history(history_data: list, user_id: int):
    """
    Procedure to print the content of riwayat.csv array from the temporary data matrix
    """
    user_hist_data = [history_data[0]]
    # Loop to check for all the user's history data
    for i in range(standard.length(history_data)):
        if history_data[i][3] == user_id:
            user_hist_data = standard.append(user_hist_data, history_data[i])

    if standard.length(user_hist_data) == 1 :
        print("Sorry, you haven't bought any game yet. Enter buy_game to buy some game.")    
    
    else :
        # generate a temporary list for hosting data without changing the source
        data_history = ["*" for i in range(standard.length(user_hist_data)-1)]
        for i in range (1, standard.length(user_hist_data)) :                # traversing from 1 to skip data heading
            data_history[i-1] = user_hist_data[i]

        # adding header to data
        header = ["ID", "NAME", "PRICE", "USER ID", "PURCHASE YEAR"]
        temp = ["*" for i in range(standard.length(data_history)+1)]  
        temp[0] = header 
        for i in range (standard.length(data_history)) :
            temp[i + 1] = data_history[i]
        
        data_history = temp

        # Generate parsing for non-empty data_history list
        for i in range (standard.length(data_history)): 
            if i == 0 :                         # skip numbering for the header
                print("  ", end= " ")
            else :                              # numbering for the list
                print(str(i) + ".", end=" ")

            for j in range (5) :
                print(data_history[i][j], end="")
                character_amount = 0

                for k in range (standard.length(data_history)):
                    if standard.length(str(data_history[k][j])) > character_amount :
                        character_amount = standard.length(str(data_history[k][j]))
                
                print((" " * (character_amount- standard.length(str(data_history[i][j])))), "| ", end="")
            print("")

"""
# Example on how to use
data = [["Header"],["1", "binomo", "15000", "3", "1990"]]
history(data)
"""
