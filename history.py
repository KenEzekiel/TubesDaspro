import readerwriter
import standard

def history(save_folder: str):
    """
    Procedure to print the content of a riwayat.csv from a save folder
    """
    data_history = readerwriter.reader(save_folder, "riwayat.csv")
    length_data = standard.length(data_history)

    if length_data == 1:
        print("Sorry, you haven't bought any game yet. Type beli_game to buy some game")
    else:
        for i in range(1, length_data):
            print(i, end=". ")
            for j in range(standard.length(data_history[i])):
                print(data_history[i][j], end=" | ")
            print("")
history("save-file-1")