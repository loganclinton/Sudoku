import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("Sudoku")
window.minsize(200, 250)
window.resizable(width=False, height=False)


def solve():
    # Backtracking algorithm
    print("test")

button = ttk.Button(text = "Check", command = solve)
button.place(x = 70, y = 205)

# Create text boxes
column = 1
row = 1
for i in range(81):
    block = ttk.Entry(window, padx = 10, pady = 10)
    block.grid(column = column, row = row)
    row += 1
    if (row > 9):
        row = 1
    if ((i+1) % 9 == 0):
        column += 1

window.mainloop()
