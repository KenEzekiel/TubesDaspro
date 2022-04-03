import os
import readerwriter

filenames = ["game.csv", "kepemilikan.csv", "riwayat.csv", "user.csv"]
#data = [readerwriter.reader("save-file-1", file) for file in filenames]
def save(folder: str, data: list):
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


#save("hai", data)