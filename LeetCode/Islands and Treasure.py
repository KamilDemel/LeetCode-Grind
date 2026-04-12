import collections
def f(grid):
    visited = set()
    kolejka_start = collections.deque()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0 and (i,j) not in visited:
                kolejka_start.append((i,j,0))
                visited.add((i,j))
    while kolejka_start:
        curr_i, curr_j, dystans = kolejka_start.popleft()
        if curr_i + 1 < len(grid) and grid[curr_i + 1][curr_j] == 2147483647 and (curr_i + 1, curr_j) not in visited:
            kolejka_start.append((curr_i + 1, curr_j,dystans+1))
            visited.add((curr_i + 1, curr_j))
            grid[curr_i+1][curr_j] = dystans + 1
        if curr_i - 1 >= 0 and grid[curr_i - 1][curr_j] == 2147483647 and (curr_i - 1, curr_j) not in visited:
            kolejka_start.append((curr_i - 1, curr_j,dystans+1))
            visited.add((curr_i - 1, curr_j))
            grid[curr_i-1][curr_j] = dystans + 1
        if curr_j + 1 < len(grid[0]) and grid[curr_i][curr_j + 1] == 2147483647 and (curr_i, curr_j + 1) not in visited:
            kolejka_start.append((curr_i, curr_j + 1,dystans+1))
            visited.add((curr_i, curr_j + 1))
            grid[curr_i][curr_j+1] = dystans + 1
        if curr_j - 1 >= 0 and grid[curr_i][curr_j - 1] == 2147483647 and (curr_i, curr_j - 1) not in visited:
            kolejka_start.append((curr_i, curr_j - 1,dystans+1))
            visited.add((curr_i, curr_j - 1))
            grid[curr_i][curr_j-1] = dystans + 1
    return grid