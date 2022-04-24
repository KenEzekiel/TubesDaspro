import F16_saver
import readerwriter

filenames = ["game.csv", "kepemilikan.csv", "riwayat.csv", "user.csv"]
data = [readerwriter.reader("save-file-1", file) for file in filenames]

def exit(data: list[list[list]]):
    # Consider this, "the input is invalid"
    # Should that confirmed to be true, the program will ask again.
    # The only acceptable inputs are the letter "y" and "n" in both lowercase or uppercase.
    x = str(input("Would you like to save the changes done? (y/n) "))
    while (x != "y") and (x != "Y") and (x != "n") and (x != "N"):
        print("")
        print("Input unidentified. Please use one of the following (y/n) ")
        x = input("Would you like to save the changes done? (y/n) ")
    if (x == "y") or (x == "Y"): # Run the save procedure and finish the program
        F16_saver.save(data)
        quit()
    elif (x == "n") or (x == "N"): # Run program as usual, allowing further use of other procedures available
        print("Understood, please use the other option available for further changes.")


# exit(data)
