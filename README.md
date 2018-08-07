# sudoku_board_checker
Simple Sudoku Board Checker

This is a simple sudoku cheker for 9 x 9 solved sudoku board. Inspired by a kata from codewars.com. It takes a list with 9 nested lists as rows.

Code first checks if there are any zeros,

second it checks each row if there is a number occured more than once,
third it makes another list with colums and checks if there is a number occured more than once,
finally it creates another sublist for 3 x 3 boxes and checks if there is a number occured more than once.

It is not very efficient however since sudoku board has a limited by 9, the code executes around 690 steps.

Example usage:

validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
])

this should return True,
