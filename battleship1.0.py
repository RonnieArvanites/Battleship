from random import randint #Imports randint

#Title and Rules
print ("Welcome to Battleship.") #Tells the user the name of the game
print ("You have 5 turns to guess the cpu's battleship location.") #Tells the user the instructions of the game
print ("Enter a row and column number located on the board.") #Tells the user what to do

#Declaration of functions used in the program
def print_board(board): #Defines the function print_board that prints the board so the user can see their guesses
  for row in board: #Displays the board in a grid
    print (" ".join(row)) #Prints each element of the list with a space between them

#Sets the range of random numbers that can be picked for the cordinates of the cpu's battleship
def random_row(board): #Defines the function random_row
  return randint(0, len(board[0])) #Returns a random integer from 1 to 5

def random_column(board): #Defines the function random_column
  return randint(0, len(board)) #Returns a random integer from 1 to 5

playagain = 1 ##Declares a variable playagain and sets it equal to 1

while playagain ==1:
    turn = 5 #Declares a variable turn and sets it equal to 5

    #Creates the board
    board = [] #Declares an empty list named board
    for x in range(5): #Creates the board
        board.append(["O"] * 5) #adds 5 zeros to the board list
    #Picks random cordinates for the cpu's battleship
    ship_row = random_row(board) #Declares a variable called ship_row and sets it to random number
    ship_column = random_column(board) #Declares a variable called ship_column and sets it to random number

    print_board(board) #Prints board

    #Main Program
    while turn > 0: #While loop that runs until turn is less than 1
        guess_row = int(raw_input("Guess Row: ")) #Asks the user to input a row
        guess_column = int(raw_input("Guess Column: ")) #Asks the user to input a column
        print (" ") #Prints a empty line
        if guess_row == ship_row and guess_column == ship_column: #If statement that checks the user's guess to see if it matches the cpu's battleship location
            print ("Congratulations! You sunk my battleship! You Win!") #Tells the user they won
            turn = 0 #Sets turn equal to 0 to end the while loop
        else: #If the user's guess does not match the cpu's battleship location then do the following
            if (guess_row < 1 or guess_row > 5) or (guess_column < 1 or guess_column > 5): #If statement that checks to make sure the user's guess is a number on the board
                print ("Oops, that's not even in the ocean. Try Again!") #Tells the user that their guess is not on the board
            elif (board[guess_row-1][guess_column-1] == "X"): #Checks whether the user's guess is a previous guess
                print ("You guessed that one already. Try Again!") #Tells the user that they guessed that position already
            else: #If the user's guess is new, on the board, and not the cpu's battleship location
                print ("You missed my battleship! Try Again!") #Tells the user they missed the cpu's battleship
                turn = turn -1 #Subtracts 1 turn from the user's total turn
                print ("Turns left: %s" % (turn)) #Tells the user how many turns they have left
                board[guess_row-1][guess_column-1] = "X" #Inserts an X where the user guessed
                print_board(board) #Displays the board
    if turn == 0: #If statement that checks if the user's turn is equal to 0
        print ("You loose. Game Over!") #Tells the user they lost
        print ("Do you want to try again!") #Asks the user if they want to try again
        playagain = int(raw_input("Enter 1 to play again or 0 to quit: ")) #Asks the user for an answer to if they want to play again
    if playagain == 0: #If statement that checks whether the user chose to play again
        print ("Thank you for playing!") #Tells the user thanks for playing
