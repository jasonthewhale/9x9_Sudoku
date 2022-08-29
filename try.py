"""
CSSE1001 Assignment 1
Semester 2, 2022
"""
from a1_support import *


# Fill these in with your details
__author__ = "Junchen You"
__email__ = "junchen.you@uq.net.au"
__date__ = "20/08/2022"


# Write your functions here
def load_board(filename: str) -> str:
    """ Reads a board file and creates a string containing all the rows in order.

    Parameters:
        filename: The path to the game file

    Returns:
        A single string containing of all rows in the board.

    >>> load_board("../boards/board_one.txt")
    '68513  477      1  1 764 5 9   7 5 48 1  9 724 3  6      42739  4 9   681 7   4  '
    """
    board = ""
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('-'):
                line = line.replace("|","")
                line = line.replace("\n","") # BW file.readlines() should do this
                board += line
    return board

def num_hours() -> float:
    return 22.22

def read_board(raw_board: str) -> "Board":
    """ Convert the string board into a list of list board (space -> None, string -> int).

    Parameters:
        raw_board: The original string board.
    
    Returns:
        A list of list board ([[...],[...],[...]]).

    >>> read_board(board_one)
    [[6, 8, 5, 1, 3, 2, 9, 4, 7], [7, 3, 4, 5, 9, 8, 2, 1, 6],
    [2, 1, 9, 7, 6, 4, 8, 5, 3], [9, 2, 6, 8, 7, 1, 5, 3, 4],
    [8, 5, 1, 3, 4, 9, 6, 7, 2], [4, 7, 3, 2, 5, 6, 1, 8, 9],
    [5, 6, 8, 4, 2, 7, 3, 9, 1], [3, 4, 2, 9, 1, 5, 7, 6, 8],
    [1, 9, 7, 6, 8, 3, 4, 2, None]]
    """
    list_board = [] 
    final_board = []                
    for x in raw_board:
        if x == " ":                            
            list_board.append(None)
        else:                      
            x = int(x)                          
            list_board.append(x)
    for i in range(0,len(list_board),9):        # Iterate the whole list with step of 9
        final_board.append(list_board[i:i+9])   # Add these seperate lists into a whole list--final_borad     
    board = final_board
    return board

def is_empty(position: tuple[int, int], board: "Board") -> bool:
    """ Check if the value of a specific position is None.

    Parameters:
        position: row and column of the specific locatin.
        board: target board that needs a check.

    Returns:
        Boolean value (True or False).

    >>> is_empty((3,5), board_three)
    False
    """
    row = position[0]
    column = position[1]
    if board[int(row)][int(column)] == None:
        return True
    else:
        return False

def update_board(position: tuple[int, int], value: int, board: "Board") -> None:
    """ Change the value of designated position into a provied value.

    Parameters:
        position: row and column of the specific locatin.
        board: target board that needs to change.

    >>> update_board((8, 8), 5, board_three)
    >>> board_three
    [[6, 8, 5, 1, 3, 2, 9, 4, 7], [7, 3, 4, 5, 9, 8, 2, 1, 6],
    [2, 1, 9, 7, 6, 4, 8, 5, 3], [9, 2, 6, 8, 7, 1, 5, 3, 4],
    [8, 5, 1, 3, 4, 9, 6, 7, 2], [4, 7, 3, 2, 5, 6, 1, 8, 9],
    [5, 6, 8, 4, 2, 7, 3, 9, 1], [3, 4, 2, 9, 1, 5, 7, 6, 8],
    [1, 9, 7, 6, 8, 3, 4, 2, 5]]
    """ 
    row = position[0]
    column = position[1]
    board[int(row)][int(column)] = value

def clear_position(position: tuple[int, int], board: "Board") -> None:  
    """ Clear the value of designated position.

    Parameters:
        position: row and column of the specific locatin.
        board: target board that needs to make a clearance.
    
    Returns:
        None.
        
    >>> clear_position((8,6), board_three)
    >>> board_three
    [[6, 8, 5, 1, 3, 2, 9, 4, 7], [7, 3, 4, 5, 9, 8, 2, 1, 6],
    [2, 1, 9, 7, 6, 4, 8, 5, 3], [9, 2, 6, 8, 7, 1, 5, 3, 4],
    [8, 5, 1, 3, 4, 9, 6, 7, 2], [4, 7, 3, 2, 5, 6, 1, 8, 9],
    [5, 6, 8, 4, 2, 7, 3, 9, 1], [3, 4, 2, 9, 1, 5, 7, 6, 8],
    [1, 9, 7, 6, 8, 3, None, 2, None]]
    """
    row = position[0]
    column = position[1]
    board[int(row)][int(column)] = None

def has_won(board) -> bool:
    """ Determine if the game has won (every row and column are 1-9 and every square is filled by 1-9).

    Parameters:
        board: target board that needs to check if win.

    Return:
        Boolean value (True or False).

    >>> has_won(board_three)
    False
    >>> update_board((8, 8), 6, board_three)
    >>> has_won(board_three)
    True
    """
    col = []
    n = 0
    count1 = 0
    count2 = 0
    count3 = 0
    square = []
    win = [1,2,3,4,5,6,7,8,9]
    for j in range(3):
        for k in range(3):
            for i in range(3*k,3*(k+1)):
                square = square + board[i][3*j:3*(j+1)] # Put 3x3 value into "square"
            if set(square) == set(win):     # Compare the values of each square  with [1,2...9], \
                count3 += 1                 # ignoring the order
            square = []
    for b in range(9):
        line = board[b]
        if set(line) == set(win):           # Compare the values of each line  with [1,2...9], \
            count1 += 1                     # ignoring the order
        for c in range(9):
            col1 = board[c][n]
            col.append(col1)
        if n < 8:
            n += 1
        else:
            n = 0
        if  set(col) == set(win):           # Compare the values of each column with [1,2...9], \
            count2 += 1                     # ignoring the order
        col = []
    if count1 == 9 and count2 ==9 and count3 == 9: # Check if every line, column and square \
        return True                                # are filled by 1-9.
    else:
        return False

def print_board(board: "Board") -> None:
    """ Transform the list of list board into a board with required format.

    Parameters:
        board: target board that needs to change format.

    >>> print_board(board_three)
    685|132|947 0
    734|598|216 1
    219|764|853 2
    -----------
    926|871|534 3
    851|349|672 4
    473|256|189 5
    -----------
    568|427|391 6
    342|915|768 7
    197|683|42  8

    012 345 678
    """
    space_board = ""
    board_3 = []
    former = []
    line = ""
    k = 0
    for i in range(9):
        for v in board[i]:
            if v != None:
                space_board = space_board + str(v)
            else:
                v = " "
                space_board = space_board + str(v)
        while k < 9:
            if k % 3 == 0:
                board_3.append(space_board[k:k+3]) # Divide every line into 3 parts.
            k += 1
        former = "|".join(board_3)                 # Add "|" between each part.
        line = former + (" ") + str(i)             # Add number of row behind the "former".
        k=0                                        # "former" means first 9 values without \ 
        if i == 2 or i ==5:                        # " " and row number in the end.
            print(line)
            print("-----------")                   # Add dividing line (dash).
        elif i == 8:
            print(line)
            print("\n012 345 678")                 # Add column number.
        else:
            print(line)
        board_3 = []                               # Initialize "board_3", "line" and "space_board",\
        line = ""                                  # so that for loop can do the work for other lines.
        space_board = ""

def main() -> None:
    """ Process the game and pop up help info when necessary.
    """ 
    file = input("Please insert the name of a board file: ")
    raw_board = read_board(load_board(file))
    game = [x[:] for x in raw_board]                # Creat a new list "game" to prevent changing \
    print_board(game)                               # original board--"raw_board"
    while 1:
        if has_won(game):
            print("Congratulations, you won!" )
            determine = input("Would you like to start a new game (y/n)? ")
            if determine == "n" or determine == "N":
                break
            else:
                file = input("Please insert the name of a board file: ")
                raw_board = read_board(load_board(file))
                game = [x[:] for x in raw_board]
                print_board(game)
        else:
            move = input("Please input your move: ")
            if move == "H" or move == "h":
                print("Need help?\nH = Help\nQ = Quit\nHint: Make sure each row, column, \
and square contains only one of each number from 1 to 9.")
                print()                               # Print a line between help info and board
                print_board(game)
            elif move == "Q" or move == "q":
                break
            elif "C" in move:
                if is_empty((move[0],move[2]),raw_board):
                    clear_position((move[0],move[2]),game)
                    print_board(game)
                else:
                    print("That move is invalid. Try again!")
                    print_board(game)
            else:
                if is_empty((move[0],move[2]),raw_board):
                    update_board((move[0],move[2]), int(move[4]), game)
                    print_board(game)
                else:
                    print("That move is invalid. Try again!")
                    print_board(game)

if __name__ == "__main__":
    main()
