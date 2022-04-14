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
        print("NO | ID | NAMA | HARGA | USER ID | TAHUN BELI")
        for i in range(1, length_data):
            print(i, end=". ")
            for j in range(standard.length(data_history[i])):
                print(data_history[i][j], end=" | ")
            print("")

def historyFromMatrix(hist_data: list):
    """
    Procedure to print the content of riwayat.csv array from the temporary data matrix
    """
    
    length_data = standard.length(hist_data)

    if length_data == 1:
        print("Sorry, you haven't bought any game yet. Type beli_game to buy some game")
    else:
        print("NO | ID | NAMA | HARGA | USER ID | TAHUN BELI")
        for i in range(1, length_data):
            print(i, end=". ")
            for j in range(standard.length(hist_data[i])):
                print(hist_data[i][j], end=" | ")
            print("")
