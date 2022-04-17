import standard

def history(hist_data: list):
    """
    Procedure to print the content of riwayat.csv array from the temporary data matrix
    """

    if standard.length(hist_data) == 1 :
        print("Sorry, you haven't bougth any game yet. Enter buy_game to bur some game.")    
    
    else :
        # generate a temporary list for hosting data without changing the source
        data_history = ["*" for i in range(standard.length(hist_data)-1)]
        for i in range (1, standard.length(hist_data)) :                # traversing from 1 to skip data heading
            data_history[i-1] = hist_data[i]

        data_history = standard.append(["NUM", "ID", "NAME", "PRICE", "USER ID", "PURCHASE YEAR"], data_history)

        # Generate parsing for non-empty data_history list
        for i in range (standard.length(data_history)): 
            print(str(i+1) + ".", end=" ")

            for j in range (6) :
                print(data_history[i][j], end="")
                character_amount = 0

                for k in range (standard.length(data_history)):
                    if standard.length(str(data_history[k][j])) > character_amount :
                        character_amount = standard.length(str(data_history[k][j]))
                
                print((" " * (character_amount- standard.length(str(data_history[i][j])))), "| ", end="")
            print("")