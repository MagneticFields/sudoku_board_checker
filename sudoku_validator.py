def valid_solution(board):
    for x in range(len(board)):  # checks the entire board if there are any zeros
        if board[x].count(0) >= 1:
            return False
            
    for i in range(1,10): # This loop iterates throught rows and checks if there are any number occured once
        if  board[x].count(i) > 1:
            return False
    vertical = []
    
    for x in range(len(board)): # this loop creates a list from columns and checks if there is any nubmber occured more than once
        for y in range(len(board)):
            vertical.append(board[y][x])
        for i in range(1,10):
            if vertical.count(i) > 1:
                return False
        vertical =[]
     
    # the code below seems inefficient since it is coded with every index number. I am sure there is a more clever hack for this.
    threes =[] # this loops creates a list from 3 X 3 boxes and checks again if the number occured more than once
    for i in range(0, 7, 3):
        for j in range(0,7,3):
            threes.append(board[i][j])
            threes.append(board[i][j+1])
            threes.append(board[i][j+2])
            threes.append(board[i +1][j])
            threes.append(board[i + 1][j + 1])
            threes.append(board[i + 1][j + 2])
            threes.append(board[i + 2][j])
            threes.append(board[i + 2][j +1])
            threes.append(board[i + 2][j + 2])
            for k in range(1,10):
                if threes.count(k) > 1:
                    return False
            threes = []
    

    return True
