"""
Made by Logan Clinton

How to change board:
Lines 19 to 27 are the current board.
The 0's represent blank spots, fill the
board in with numbers you want and put 0's
in the spots you want to leave blank.
Make sure there are 9 numbers across and 9 numbers downwards.
Make surethere are commas in between each number (at the end of the line too)


"""
import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("Sudoku")
window.minsize(200, 250)
window.resizable(width=False, height=False)

# 0's represent blank spaces
puzzle = [0, 6, 0, 0, 1, 0, 9, 0, 0,
          3, 0, 1, 0, 4, 0, 2, 0, 5,
          4, 0, 5, 7, 2, 8, 6, 0, 0,
          0, 0, 0, 2, 0, 0, 0, 0, 0,
          0, 0, 8, 6, 9, 5, 3, 0, 0,
          0, 0, 0, 0, 0, 1, 0, 0, 0,
          0, 0, 4, 8, 5, 9, 1, 0, 7,
          5, 0, 7, 0, 6, 0, 4, 0, 3,
          0, 0, 9, 0, 7, 0, 0, 6, 0]

def printBoard():
    column = 1
    row = 1
        
    for i in range(81):
        block = ttk.Entry(window, width = 3)
        block.grid(column = column, row = row)
        num = "  " + str(puzzle[i])
        if (puzzle[i] != 0):
            block.insert(tk.INSERT, num)
            block.config(state="disabled")
        row += 1
        if (row > 9):
            row = 1
        if ((i+1) % 9 == 0):
            column += 1

# Uses backtracking algorithm to solve the board
def solve():
    
    printBoard()


button = ttk.Button(text = "Solve", command = solve)
button.place(x = 70, y = 205)

# Create text boxes
printBoard()


window.mainloop()
