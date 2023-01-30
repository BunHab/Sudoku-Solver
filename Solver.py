def print_board(board):
    '''
    This function takes a 2D list representing a sudoku board as input and prints the board. 
    It formats the board in a 9x9 grid format, with vertical bars between sub-grids and horizontal lines separating sub-grids.
    '''
    boardString = ''
    for i in range(9):
        for j in range(9):
            boardString += str(board[i][j]) + ' '
            if (j + 1) % 3 == 0 and j != 0 and j + 1 != 9:
                boardString += '| '

            if j == 8:
                boardString += '\n'

            if j == 8 and (i + 1) % 3 == 0 and i + 1 != 9:
                boardString += '- - - - - - - - - - - \n'
    print(boardString)

def solve_sudoku(grid):

    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    for num in range(1, 10):
        if is_valid(grid, (row, col), num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

def find_empty_cell(grid):
    '''
    This function takes a 2D list representing a sudoku board as input and returns the position of the first empty cell in the grid.
    '''
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)

    return None

def is_valid(grid, pos, num):
    '''
    This function takes a 2D list representing a sudoku board, a position in the grid, and a number as input, 
    and returns True if the number is a valid solution for the position in the grid, False otherwise.
    '''
    # check if the number is already in the same row
    for col in range(9):
        if grid[pos[0]][col] == num:
            return False

    # check if the number is already in the same column
    for row in range(9):
        if grid[row][pos[1]] == num:
            return False

    # check if the number is already in the same square
    square_x, square_y = pos[1] // 3, pos[0] // 3

    for row in range(square_y * 3, square_y * 3 + 3):
        for col in range(square_x * 3, square_x * 3 + 3):
            if grid[row][col] == num:
                return False

    return True