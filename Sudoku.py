import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("Sudoku")
window.minsize(200, 250)
window.resizable(width=False, height=False)

puzzle = [0, 6, 0, 0, 1, 0, 9, 0, 0,
          3, 0, 1, 0, 4, 0, 2, 0, 5,
          4, 0, 5, 7, 2, 8, 6, 0, 0,
          0, 0, 0, 2, 0, 0, 0, 0, 0,
          0, 0, 8, 6, 9, 5, 3, 0, 0,
          0, 0, 0, 0, 0, 1, 0, 0, 0,
          0, 0, 4, 8, 5, 9, 1, 0, 7,
          5, 0, 7, 0, 6, 0, 4, 0, 3,
          0, 0, 9, 0, 7, 0, 0, 6, 0]

def solve():
    # Backtracking algorithm
    print("test")

button = ttk.Button(text = "Check", command = solve)
button.place(x = 70, y = 205)

# Create text boxes
column = 1
row = 1
for i in range(81):
    block = ttk.Entry(window, width = 3)
    block.grid(column = column, row = row)
    if (puzzle[i] != 0):
        block.insert(tk.INSERT, puzzle[i])
    else:
        print("Done.")
    row += 1
    if (row > 9):
        row = 1
    if ((i+1) % 9 == 0):
        column += 1

        

window.mainloop()
