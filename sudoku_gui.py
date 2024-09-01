import ctypes
from tkinter import *

# Full path to the shared library
dll_path = r'C:\Users\ASUS\OneDrive\Desktop\python\sudoku\solver.dll'

# Load the shared library
try:
    solver = ctypes.CDLL(dll_path)
except Exception as e:
    print(f"Error loading library: {e}")
    exit()

# Define the function prototypes
solver.solve.argtypes = [ctypes.POINTER(ctypes.c_int)]
solver.solve.restype = ctypes.c_bool

def solve_sudoku():
    # Convert the grid to a 1D array for C++ compatibility
    sudoku = []
    for i in range(9):
        for j in range(9):
            try:
                num = int(entries[i][j].get())
            except ValueError:
                num = 0
            sudoku.append(num)

    # Convert the Python list to a C array
    sudoku_array = (ctypes.c_int * 81)(*sudoku)

    # Call the C++ solver
    try:
        if solver.solve(sudoku_array):
            # Update the grid with the solution
            for i in range(9):
                for j in range(9):
                    entries[i][j].delete(0, END)
                    entries[i][j].insert(0, str(sudoku_array[i * 9 + j]))
        else:
            print("No solution exists")
    except Exception as e:
        print(f"Error calling C++ function: {e}")

# Tkinter GUI setup
root = Tk()
root.title("Sudoku Solver")

entries = []
for i in range(9):
    row = []
    for j in range(9):
        entry = Entry(root, width=2, font=('Arial', 18), justify='center')
        entry.grid(row=i, column=j)
        row.append(entry)
    entries.append(row)

solve_button = Button(root, text="Solve", command=solve_sudoku)
solve_button.grid(row=9, column=0, columnspan=9)

root.mainloop()
