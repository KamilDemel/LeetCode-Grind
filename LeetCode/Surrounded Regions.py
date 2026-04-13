import collections
def f(board):
    kolejka = collections.deque()
    visited = set()
    for i in range(len(board)):
        if board[i][0] == "O":
            kolejka.append((i,0))
            visited.add((i,0))
        if board[i][len(board[0]) - 1] == "O":
            kolejka.append((i, len(board[0]) - 1))
            visited.add((i, len(board[0]) - 1))
    for j in range(len(board[0])):
        if board[0][j] == "O":
            kolejka.append((0,j))
            visited.add((0,j))
        if board[len(board) - 1][j] == "O":
            kolejka.append((len(board) - 1,j))
            visited.add((len(board) - 1,j))
    while kolejka:
        curr_i, curr_j = kolejka.popleft()
        visited.add((curr_i,curr_j))
        if 0 <= curr_i < len(board) and 0 <= curr_j < len(board[0]):
            board[curr_i][curr_j] = "T"
        if curr_i + 1 < len(board) and board[curr_i + 1][curr_j] == "O" and (curr_i + 1, curr_j) not in visited:
            kolejka.append((curr_i + 1, curr_j))
            visited.add((curr_i + 1, curr_j))
            board[curr_i+1][curr_j] = "T"
        if curr_i - 1 >= 0 and board[curr_i - 1][curr_j] == "O" and (curr_i - 1, curr_j) not in visited:
            kolejka.append((curr_i - 1, curr_j))
            visited.add((curr_i - 1, curr_j))
            board[curr_i-1][curr_j] = "T"
        if curr_j + 1 < len(board[0]) and board[curr_i][curr_j + 1] == "O" and (curr_i, curr_j + 1) not in visited:
            kolejka.append((curr_i, curr_j + 1))
            visited.add((curr_i, curr_j + 1))
            board[curr_i][curr_j+1] = "T"
        if curr_j - 1 >= 0 and board[curr_i][curr_j - 1] == "O" and (curr_i, curr_j - 1) not in visited:
            kolejka.append((curr_i, curr_j - 1))
            visited.add((curr_i, curr_j - 1))
            board[curr_i][curr_j-1] = "T"
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "X" or board[i][j] == "O":
                board[i][j] = "X"
            else:
                board[i][j] = "O"
