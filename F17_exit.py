def exit(x):
    # Consider this, "the input is invalid"
    # Should that confirmed to be true, the program will ask again.
    # The only acceptable inputs are the letter "y" and "n" in both lowercase or uppercase.
    while (x != "y") and (x != "Y") and (x != "n") and (x != "N"):
        print("")
        print("Input unidentified. Please use one of the following (y/n) ")
        x = input("Would you like to save the changes done? (y/n) ")
    if (x == "y"): # Run the save procedure and finish the program
        quit()
    elif (x == "n"): # Run program as usual, allowing further use of other procedures available
        print("Understood, please use the other option available for further changes.")

x = str(input("Would you like to save the changes done? (y/n) "))
exit(x)
