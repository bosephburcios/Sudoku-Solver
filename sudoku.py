def sudoku_solver(puzzle):
    
    row, col = find_empty(puzzle) # finds the next empty square in the puzzle (i.e. -1)
    
    if row is None:
        return True
    
    # once a place is found, make a guess from 1 - 9
    for guess in range(1, 10):
        # checks for valid guess
        if isValid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            
            # recursively call the function
            if sudoku_solver(puzzle):
                return True    
        puzzle[row][col] = -1 # if not valid
    return False
    
def find_empty(puzzle):
    
    # checks each row and column for a spot that had not been guessed yet or an empty square
    for r in range(9): 
        for c in range(9):
            if(puzzle[r][c] == -1): # if empty return coordinates
                return r, c
    return None, None # else return none to signal that every space is filled

def isValid(puzzle, guess, row, col):
    
    # checks if guess in row is valid
    row_num = puzzle[row]
    if guess in row_num:
        return False
    
    # same thing but for column
    col_num = []
    
    # for each row we will append the value in puzzle at the ith row and the col column
    for i in range(9):
        col_num.append(puzzle[i][col])
    if guess in col_num:
        return False
    
    # see where the 3x3 starts and iterates over the 3 values in the row/column
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    # is a valid guess
    return True

if __name__ == '__main__':
    example_board = [
        [5, 3, -1,  -1, 7, -1,  -1, -1, -1],
        [6, -1, -1,  1, 9, 5,  -1, -1, -1],
        [-1, 9, 8,  -1, -1, -1,  -1, 6, -1],
        
        [8, -1, -1,  -1, 6, -1,  -1, -1, 3],
        [4, -1, -1,  8, -1, 3,  -1, -1, 1],
        [7, -1, -1,  -1, 2, -1,  -1, -1, 6],
        
        [-1, 6, -1,  -1, -1, -1,  2, 8, -1],
        [-1, -1, -1,  4, 1, 9,  -1, -1, -5],
        [-1, -1, -1,  -1, 8, -1,  -1, 7, 9]
    ]
    print(sudoku_solver(example_board))
    print(example_board)
