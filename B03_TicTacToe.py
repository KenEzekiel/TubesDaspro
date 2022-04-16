import standard

# not to be imported    
def ask_location(matrix : list, pawn : str):
    """
    Procedure to ask input for pawn location and validate it.
    """
    valid = False
    while valid == False :
        print(pawn, "turn: ")
        x = int(input("X: "))
        y = int(input("Y: "))

        # Location validation
        if not((1<=x<=3) and (1<=y<=3) ):   # the location does not exist
            print("Invalid location. Please try again!")
        else :                              # the location exists

            if matrix[y-1][x-1] != "#":     # the location is alrady occupied
                print("Invalid location. Please try again!")
            else :                          # teh location is empty
                matrix[y-1][x-1] = pawn
                valid = True

# not to be imported
def win_checker(matrix : list, pawn : str) -> str: 
    """
    Function to return state of winning of a pawn
    """
    win = ""        # win = "" --> pawn haven't won yet

    # horizontal win checker
    if ((matrix [0][0] == pawn) and (matrix [0][1] == pawn) and (matrix [0][2] == pawn)) or ((matrix [1][0] == pawn) and (matrix [1][1] == pawn) and (matrix [1][2] == pawn)) or ((matrix [2][0] == pawn) and (matrix [2][1] == pawn) and (matrix [2][2] == pawn)):
        win = "horizontally"
    
    # vertical win checker
    elif ((matrix [0][0] == pawn) and (matrix [1][0] == pawn) and (matrix [2][0] == pawn)) or ((matrix [0][1] == pawn) and (matrix [1][1] == pawn) and (matrix [2][1] == pawn)) or ((matrix [0][2] == pawn) and (matrix [1][2] == pawn) and (matrix [2][2] == pawn)) :
        win = "vertically"
    
    # diagonal win checker
    elif ((matrix [0][0] == pawn) and (matrix [1][1] == pawn) and (matrix [2][2] == pawn)) or ((matrix [0][2] == pawn) and (matrix [1][1] == pawn) and (matrix [2][0] == pawn)):
        win = "diagonally"

    return win

# not to be imported
def status(matrix : list) :
    """
    Procedure to print out board status.
    """
    print("=============")
    print("Board Status:")

    # Generate parsing for matrix
    for i in range (3): 
        print("|", end=" ")
        for j in range (3) :
            print(matrix[i][j], end=" ")
            print("|", end=" ")
        print("")

def tictactoe ():
    """
    Procedure to simulate tic tac toe game
    """
    matrix = [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]]
    turn = 0 

    while (turn<=9): 
        turn += 1

        if turn%2 == 1 :
            pawn = "X"
        else :
            pawn = "O"
        
        status(matrix)                  # print out board status
        ask_location(matrix, pawn)      # ask for user input of pawn location

        # check if pawn wins 
        win = win_checker(matrix, pawn)
        if win != "":                   # (win = "")--> meaning pawn haven't won yet 
            status(matrix)
            if win == "horizontally" :
                print(pawn, "won horizontally. Victory applies to other row.")
            elif win == "vertically" :
                print(pawn, "won vertically. Victory applies to other column.")
            else :          # win == "diagonally"
                print(pawn, "won diagonally. Victory applies to the opposite diagonal.")

            break

        else :              # win == "" --> pawn haven't won
            pass

        # turn == 9 is the last turn; tie statement will be skipped if there is already a winner
        if turn == 9 :
            status(matrix)
            print("Tie. There is no winner.")
            break


# Example on how to use
# tictactoe()