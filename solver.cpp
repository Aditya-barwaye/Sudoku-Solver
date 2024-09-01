#include <vector>

extern "C" {
    __declspec(dllexport) bool isSafe(int row, int col, int value, int sudoku[9][9]) {
        for (int i = 0; i < 9; i++) {
            if (sudoku[i][col] == value) return false; // Check column
            if (sudoku[row][i] == value) return false; // Check row
            if (sudoku[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == value) return false; // Check 3x3 grid
        }
        return true;
    }

    __declspec(dllexport) bool solve(int sudoku[9][9]) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (sudoku[i][j] == 0) { // Find an empty cell
                    for (int k = 1; k <= 9; k++) {
                        if (isSafe(i, j, k, sudoku)) {
                            sudoku[i][j] = k;
                            if (solve(sudoku)) return true; // Recursively try to solve
                            sudoku[i][j] = 0; // Undo assignment if it leads to no solution
                        }
                    }
                    return false; // No valid number found, trigger backtracking
                }
            }
        }
        return true; // Solved
    }
}
