import collections
def f(grid):
    visited = set()
    max_pole = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1 and (i,j) not in visited:
                visited.add((i,j))
                kolejka = collections.deque()
                kolejka.append((i,j))
                ctr = 1
                while kolejka:
                    curr_i, curr_j = kolejka.popleft()
                    if curr_i + 1 < len(grid) and grid[curr_i+1][curr_j] == 1 and (curr_i+1,curr_j) not in visited:
                        kolejka.append((curr_i+1,curr_j))
                        visited.add((curr_i+1,curr_j))
                        ctr += 1
                    if curr_i - 1 >= 0 and grid[curr_i-1][curr_j] == 1 and (curr_i-1,curr_j) not in visited:
                        kolejka.append((curr_i-1,curr_j))
                        visited.add((curr_i-1,curr_j))
                        ctr += 1
                    if curr_j + 1 < len(grid[i]) and grid[curr_i][curr_j+1] == 1 and (curr_i,curr_j+1) not in visited:
                        kolejka.append((curr_i,curr_j+1))
                        visited.add((curr_i,curr_j+1))
                        ctr += 1
                    if curr_j - 1 >= 0 and grid[curr_i][curr_j-1] == 1 and (curr_i,curr_j-1) not in visited:
                        kolejka.append((curr_i,curr_j-1))
                        visited.add((curr_i,curr_j-1))
                        ctr += 1
                if ctr > max_pole:
                    max_pole = ctr
    return max_pole