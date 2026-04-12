import collections
def f(grid):
    visited = set()
    kolejka = collections.deque()
    ile_pomaranczy_swiezych = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                ile_pomaranczy_swiezych += 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2 and (i,j) not in visited:
                visited.add((i,j))
                kolejka.append((i,j,0))
    ctr = 0
    minuty = 0
    while kolejka:
        curr_i, curr_j,dystans = kolejka.popleft()
        if curr_i + 1 < len(grid) and grid[curr_i + 1][curr_j] == 1 and (curr_i + 1,curr_j) not in visited:
            kolejka.append((curr_i + 1, curr_j,dystans+1))
            visited.add((curr_i + 1, curr_j))
            grid[curr_i + 1][curr_j] = 2
            minuty = dystans + 1
            ctr += 1
        if curr_i - 1 >= 0 and grid[curr_i - 1][curr_j] == 1 and (curr_i - 1, curr_j) not in visited:
            kolejka.append((curr_i - 1, curr_j,dystans+1))
            visited.add((curr_i - 1, curr_j))
            grid[curr_i - 1][curr_j] = 2
            minuty = dystans + 1
            ctr += 1
        if curr_j + 1 < len(grid[0]) and grid[curr_i][curr_j + 1] == 1 and (curr_i,curr_j + 1) not in visited:
            kolejka.append((curr_i, curr_j + 1,dystans+1))
            visited.add((curr_i, curr_j + 1))
            grid[curr_i][curr_j + 1] = 2
            minuty = dystans + 1
            ctr += 1
        if curr_j - 1 >= 0 and grid[curr_i][curr_j - 1] == 1 and (curr_i, curr_j - 1) not in visited:
            kolejka.append((curr_i, curr_j - 1,dystans+1))
            visited.add((curr_i, curr_j - 1))
            grid[curr_i][curr_j - 1] = 2
            minuty = dystans + 1
            ctr += 1
    if ctr == ile_pomaranczy_swiezych:
        return minuty
    else:
        return -1