import random
import copy

# Blank board at the start of game. We will start with a blank list and then add to this blank board through using a variety of functions.
board = []
# This function will initially fill the board with 0's in all cells. (Please note that all cells containing 0's will appear as blank spaces in the final game - refer to the 'display()' function.)
for i in range(4):
    row = []
    # Here we are appending the 0's to each empty row.
    for j in range(4):
        row.append(0)
    # We then append all four empoty rows to the board.
    board.append(row)

# <-- After defining our board at the very top, all function definitions have been placed here below this point. -->

# We need to create a 'display' function that will display the board in a 4 * 4 grid in our terminal.
def display():
    # We must first find the largest value in our board so that we can appropriately size each of the cells. For example:
    # As we can see below, the lines in the board do not line up as some values are longer than others:
    # | | |2048|2|
    # |128|2|2|256|
    # |4|16| |4|
    # | |2| |32|
    # Our goal is for the board to look something like below. As we can see, 2048 is the largest number with 4 characters, therefore we want each of the cells to be 4 characters wide:
    # |    |    |2048|   2|
    # | 128|   2|   2| 256|
    # |   4|  16|    |   4|
    # |    |   2|    |  32|
    # Starting at the very first cell in the first row.
    largest = board[0][0]
    # Looping through each row in the board.
    for row in board:
        # Then we loop through each cell in the row.
        for cell in row:
            # If the current value is bigger than the largest value, it is now assigned as the new largest value.
            if cell > largest:
                largest = cell
    
    # We will then store the length of the largest number in 'number_of_spaces'. We need to convert it to a string so we can use the 'len()' function.
    number_of_spaces = len(str(largest))

    # This loop will look through every row in the board.
    for row in board:
        # I would like the board to have vertical lines between each column in the 4 * 4 grid.
        current_row = '|'
        # This loop will now look through each individual cell in the row.
        for cell in row:
            # If the cell has a value of 0, I would like the cell to be empty. However, it is important that the cell is still as wide as the largest number on the board, therefore we multiply the amount of empty spaces by 'number_of_spaces' (which contains the length of the largest number).
            if cell == 0:
                current_row += ' ' * number_of_spaces + '|'
            # If the cell has a value greater than 0, I would like to display the value in the cell. I would like to display this value as a string instead of an integer so I can use the 'len()' function on it. Again, it is important that the cell is equivalent in width to the largest number on the board. As our numbers can vary in length, we cannot simply add 'number_of_spaces' to our number, instead we must calculate the difference in characters between the largest number and the number in the cell. For example, if the largest number on the board is '1024' we must add 2 empty spaces to '16', or 3 empty spaces to '2', or 1 empty space to '128'. As such, we subtract the length of the number in our current cell from the largest number, then we multiply our empty spaces by the result of this calculation. Finally, we can add our current number to the cell.
            else:
                current_row += (' ' * (number_of_spaces - len(str(cell)))) + str(cell) + '|'
        # I would now like to display the generated row.
        print(current_row)

# This function will merge one row to the left. We will take one row as an input.
def merge_one_row_left(row):
    # We must first move everything within the row as far left as possible. 
    # We first need a for loop that will scan all cells, starting from right to left.
    for i in range(3):
        for j in range(3, 0, -1):
            # We have to test whether or not there is an empty space to the left of each cell (current cell - 1). If there is an empty space, then we shift to that space.
            if row[j - 1] == 0:
                # If there is an empty space, we need to replace the empty cell with the number in our current cell (essentially shifting the number to the left).
                row[j - 1] = row[j]
                # As we are shifting left, the previous cell of the number must be made 0 (empty).
                row[j] = 0

    # Now that the values have been pushed/compressed as far left as possible, we must actually merge any matching adjacebnt values.
    for i in range(0, 3, 1):
        # Now we test if the value in the current cell is identical to the value to the left of the current cell. If it is, then we double the value of cell to the left, and make the current cell = 0.
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    
    # Move everything to the left again as there may be still some remaining empty cells after merging (this step is essentially identical to the first step).
    for i in range(3, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    # Finally, we can return the merged row.
    return row

# Now that we can merge one row to the left, we need to now merge the whole board to the left.
def merge_left(current_board):
    # We just need to use the 'merge_one_row_left' function on each row on the board. To do this, we use a for loop.
    for i in range(4):
        # Here, we are replacing the old row with the newly merged row.
        current_board[i] = merge_one_row_left(current_board[i])
    # Then we can finally return the fully merged board.
    return current_board

# I have not included any comments for 'merge_one_row_right' and 'merge_right' as it is pretty much exactly the same as the 'merge_left' functions - the only difference is that it's reversed so it merges in the opposite direction.
def merge_one_row_right(row):
    for i in range(3):
        for j in range(0, 3, 1):
            if row[j + 1] == 0:
                row[j + 1] = row[j]
                row[j] = 0

    for i in range(3, 0, -1):
        if row[i] == row[i - 1]:
            row[i] *= 2
            row[i - 1] = 0
    
    for i in range(0, 3, 1):
        if row[i + 1] == 0:
            row[i + 1] = row[i]
            row[i] = 0
    return row

def merge_right(current_board):
    for i in range(4):
        current_board[i] = merge_one_row_right(current_board[i])
    
    return current_board

# After researching, I found that in order to create the 'merge-up' function, we must do something known as 'transposing' the entire board. Once the board is in its transposed state, we must then use the 'merge-left' function on the transposed board. After merging left, we use the transpose method again on the board to then return the board to its previous state. The end result of this will behave as if the board has merged up.
def transpose(current_board):
    # We start by looking at each row in our board.
    for i in range(4):
        # Then we must look for any elements in that row that are above the diagonal (imagine we cut the board in half, diagonally).
        for j in range(i, 4):
            # This will now check if an element is not on the diagonal.
            if not j == i:
                # If a cell is not on the diagonal, we will then swap the current element with its corresponding cell below the diagonal. To do this, we will need to create a temporary variable to hold the current value temporarily while swapping.
                temp = current_board[i][j]
                current_board[i][j] = current_board[j][i]
                current_board[j][i] = temp
    # Once transposed, we return the newly transposed board.
    return current_board

# As mentioned earlier, in order to merge-up we need to transpose the current board, then use the 'merge_left()' function on the transposed board, then transpose the board back.
def merge_up(current_board):
    # 1. Transpose the current board.
    current_board = transpose(current_board)
    # 2. Merge the board left.
    current_board = merge_left(current_board)
    # 3. Transpose the board back again.
    current_board = transpose(current_board)
    # 4. The board will now return as merged-up.
    return current_board

# I have not included any comments for merge_down() as it is identical to merge_up, except we only need to merge_right while in the transposed state.
def merge_down(current_board):
    current_board = transpose(current_board)
    current_board = merge_right(current_board)
    current_board = transpose(current_board)

    return current_board

# This function generates a new value of 2 or 4 in between each move.
def new_value():
    # I decided to use the random module to return a 4 once every 10 moves.
    if random.randint(1, 10) == 1:
        return 4
    # Therefore, 9 out of 10 moves will add a value of 2 to the board, but on the 10th move a 4 will be added instead.
    else:
        return 2

# This function will actually add a value to one of the random empty spaces on the board.
def add_new_value():
    # Here we are picking random row and column values for the new numbers to be placed.
    row_number = random.randint(0, 3)
    column_number = random.randint(0, 3)

    # This function will continually scan through random spots until it finds one that is empty, then it will add the new number to the empty spot.
    # This while loop will continue looping through random spots on the board for as long as there is a number in each space it checks. Once it finds an empty spot (cell == 0), it will retrieve a new number from 'new_value()' and place it in the random empty spot.
    while not board[row_number][column_number] == 0:
        row_number = random.randint(0, 3)
        column_number = random.randint(0, 3)
    
    # Fill the empty spot with the new value
    board[row_number][column_number] = new_value()

# This function will test if the user has won the game (i.e. the user has achieved a value of 2048).
def game_won():
    # It will scan through each row in the board.
    for row in board:
        # If it finds a cell containing 2048, game_won() = True, hence ending the game.
        if 2048 in row:
            return True
    # If it could not find a cell containing 2048, play on.
    return False

# This function will test if there are no possible moves left to be made. I found this function particularly confusing. In order to do this, we must utilise the 'copy' module.
def game_lost():
    # We first start by creating 2 temporary copies of the current board using the deepcopy function in the copy module.
    temporary_board_1 = copy.deepcopy(board)
    temporary_board_2 = copy.deepcopy(board)

    # We then use temporary_board_1 and merge it in every possible direction (up, down, left, right). After each merge, we will check if the board is still identical to temporary_board_2 (which will remain unchanged). If temporary_board_1 is identical to temporary_board_2, it demonstrates that the board could not merge any further, hence no further moves are possible.
    temporary_board_1 = merge_up(temporary_board_1)
    if temporary_board_1 == temporary_board_2:
        temporary_board_1 = merge_left(temporary_board_1)
        if temporary_board_1 == temporary_board_2:
            temporary_board_1 = merge_down(temporary_board_1)
            if temporary_board_1 == temporary_board_2:
                temporary_board_1 = merge_right(temporary_board_1)
                if temporary_board_1 == temporary_board_2:
                    # If temporary_board_1 is identical to temporary_board_2 after all possible merges have been depleted, the game has been lost, and game_lost() will == True.
                    return True
    # If there are still any possible moves to make, we will break from the above if statements and play on.
    return False


# <-- Now that we have all functions defined above, we can now use those functions to create the flow of operations to get our our 2048 game working (see below). -->

# At the very start of the game we need to fill the board with two values.
values_added = 2
while values_added > 0:
    # Using the random module again to generate random 'co-ordinates' to place our initial numbers. We do this by generating a random row number, and random column number.
    row_number = random.randint(0, 3)
    column_number = random.randint(0, 3)

    # Of course, we must only add new values to empty spaces, therefore we use the below if statement. If we are at the start of the game, all cells in the board will be empty.
    if board[row_number][column_number] == 0:
        # We then call our 'new_value()' function above to retrieve our generated numbers, and we then place our new numbers in our randomly chosen cells.
        board[row_number][column_number] = new_value()
        # After the first board setup, we only need 1 value to be added to our board in between moves, therefore we decrease our 'values_added' by 1.
        values_added -= 1

# Now that the board has been initialized, we'll welcome the user with the following message:
print("Hey there friend, welcome to 2048! The goal of this game is to combine values with the end goal of reaching the number 2048. To combine these values, you are allowed to merge in one of four different directions per move; use 'w' to merge up, 'a' to merge left, 's' to merge down and 'd' to merge right. The starting board is below, good luck! ")

# Then we'll call the 'display()' function to show the user the intitial board.
display()

# We'll use the game_over variable to keep track of whether the game has ended via the user winning or losing. Initiaily by default, we'll set it to False and we'll switch it to True only when the user wins or loses the game.
game_over = False

# For as long as the game isn't over (game_over = False), we'll repeatedly ask the user for a 'w', 'a', 's' or 'd' input for their next move.
while not game_over:
    # We'll ask the user for their move via an input statement.
    move = input("Which direction do you wish to merge? ")
    
    # By default, we'll assume the user's input is valid (either 'w', 'a', 's', or 'd').
    valid_input = True

    # Figue out which direction the user wants to merge, and then use the corresponding function to merge in the chosen direction.
    if move == 'w':
        board = merge_up(board)
    elif move == 'a':
        board = merge_left(board)
    elif move == 's':
        board = merge_down(board)
    elif move == 'd':
        board = merge_right(board)
    else:
        valid_input = False

    # If the user did not enter either 'w', 'a', 's', or 'd' - their input is invalid, therefore we'll return the following.
    if valid_input == False:
        # User will be asked to re-enter their input if they entered anything other than w, a, s, or d.
        print("Your input was invalid. Please only enter 'w', 'a', 's' or 'd'. ")
    else:
        if game_won() is True:
            display()
            print('Congratulations! You got 2048 and won the game!')
            # If player achieves 2048, display the board, congratulkate the user and update game_over to True, hence finishing the game.
            game_over = True
        # If game hasn't been won yet, add a new random value and display the new board, ready for the next move/user input.
        add_new_value()
        display()
        # After adding the new value, we'll call the game_lost() function to check if there are any possible moves left to be made. If there isn't, then it's game over, the user has lost.
        if game_lost() is True:
            print('You lost the game, there are no possible moves left to be made.')
