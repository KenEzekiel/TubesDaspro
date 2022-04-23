import os
import readerwriter
import F15_load

filenames = ["game.csv", "kepemilikan.csv", "riwayat.csv", "user.csv"]
"""
Struktur data untuk akses file per indeks = 
["game.csv", "kepemilikan.csv", "riwayat.csv", "user.csv"]
"""
# data = [readerwriter.reader("save-file-1", file) for file in filenames]

# Not to be imported
def saver(folder: str, data: list):
    """
    Procedure to save the data in the program to the database
    """
    path = f"Database/{folder}"
    exist = os.path.exists(path)
    if exist:
        # overwrite data with the new, appended data (from the main program)
        readerwriter.writeline(folder, "game.csv", data[0])
        readerwriter.writeline(folder, "kepemilikan.csv", data[1])
        readerwriter.writeline(folder, "riwayat.csv", data[2])
        readerwriter.writeline(folder, "user.csv", data[3])
    else:
        # make new folder
        os.makedirs(path)
        for file in filenames:
            open(f"{path}/{file}", "w")
        readerwriter.writeline(folder, "game.csv", data[0])
        readerwriter.writeline(folder, "kepemilikan.csv", data[1])
        readerwriter.writeline(folder, "riwayat.csv", data[2])
        readerwriter.writeline(folder, "user.csv", data[3])

# To be Imported
def save(data: list[list[list]]):
    """
    Procedure to ask whether to save in the same save folder or a different one
    """
    is_new_folder = input("Do you wish to save to a new folder? (y/n) ")
    while (is_new_folder != "y") and (is_new_folder != "Y") and (is_new_folder != "n") and (is_new_folder != "N"):
        print("Unknown input. Please choose between (y/n)")
        is_new_folder = input("Do you wish to save to a new folder? (y/n) ")
    if (is_new_folder == "y") or (is_new_folder == "Y"): 
        new_folder = input("folder name: ")
        saver(new_folder, data)
    elif (is_new_folder == "n") or (is_new_folder == "N"): 
        folder = F15_load.save_folder
        saver(folder, data)
#save("hai", data)