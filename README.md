# sudoku_board_checker
Simple Sudoku Board Checker

This is a simple sudoku cheker for 9 x 9 solved sudoku board. Inspired by a kata from codewars.com. It takes a list with 9 nested lists as rows.

Code first checks if there are any zeros,

second it checks each row if there is a number occured more than once,
third it makes another list with colums and checks if there is a number occured more than once,
finally it creates another sublist for 3 x 3 boxes and checks if there is a number occured more than once.

It is not very efficient however since sudoku board has a limited by 9, the code executes around 690 steps.
