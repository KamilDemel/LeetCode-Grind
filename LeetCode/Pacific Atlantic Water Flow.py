import collections
def f(heights):
    kolejka_pacfic = collections.deque()
    kolejka__atlantic = collections.deque()
    visited_pacific = set()
    visited_atlantic = set()
    for i in range(len(heights)):
        for j in range(len(heights[i])):
            if i == 0 and (i,j) not in kolejka_pacfic:
                kolejka_pacfic.append((i,j))
                visited_pacific.add((i,j))
            if j == 0 and (i,j) not in kolejka_pacfic:
                kolejka_pacfic.append((i,j))
                visited_pacific.add((i, j))
            if i == len(heights) - 1 and (i,j) not in kolejka__atlantic:
                kolejka__atlantic.append((i,j))
                visited_atlantic.add((i, j))
            if j == len(heights[0]) - 1 and (i,j) not in kolejka__atlantic:
                kolejka__atlantic.append((i,j))
                visited_atlantic.add((i, j))
    while kolejka_pacfic:
        curr_i,curr_j = kolejka_pacfic.popleft()
        visited_pacific.add((curr_i,curr_j))
        if curr_i + 1 < len(heights) and (curr_i+1,curr_j) not in visited_pacific and heights[curr_i+1][curr_j] >= heights[curr_i][curr_j]:
            kolejka_pacfic.append((curr_i+1,curr_j))
            visited_pacific.add((curr_i+1,curr_j))
        if curr_j + 1 < len(heights[0]) and (curr_i,curr_j+1) not in visited_pacific and heights[curr_i][curr_j+1] >= heights[curr_i][curr_j]:
            kolejka_pacfic.append((curr_i,curr_j+1))
            visited_pacific.add((curr_i,curr_j+1))
        if curr_i - 1 >= 0 and (curr_i-1,curr_j) not in visited_pacific and heights[curr_i-1][curr_j] >= heights[curr_i][curr_j]:
            kolejka_pacfic.append((curr_i-1,curr_j))
            visited_pacific.add((curr_i-1,curr_j))
        if curr_j - 1 >= 0 and (curr_i,curr_j-1) not in visited_pacific and heights[curr_i][curr_j-1] >= heights[curr_i][curr_j]:
            kolejka_pacfic.append((curr_i,curr_j-1))
            visited_pacific.add((curr_i,curr_j-1))
    while kolejka__atlantic:
        curr_i,curr_j = kolejka__atlantic.popleft()
        visited_atlantic.add((curr_i,curr_j))
        if curr_i + 1 < len(heights) and (curr_i+1,curr_j) not in visited_atlantic and heights[curr_i+1][curr_j] >= heights[curr_i][curr_j]:
            kolejka__atlantic.append((curr_i+1,curr_j))
            visited_atlantic.add((curr_i+1,curr_j))
        if curr_j + 1 < len(heights[0]) and (curr_i,curr_j+1) not in visited_atlantic and heights[curr_i][curr_j+1] >= heights[curr_i][curr_j]:
            kolejka__atlantic.append((curr_i,curr_j+1))
            visited_atlantic.add((curr_i,curr_j+1))
        if curr_i - 1 >= 0 and (curr_i-1,curr_j) not in visited_atlantic and heights[curr_i-1][curr_j] >= heights[curr_i][curr_j]:
            kolejka__atlantic.append((curr_i-1,curr_j))
            visited_atlantic.add((curr_i-1,curr_j))
        if curr_j - 1 >= 0 and (curr_i,curr_j-1) not in visited_atlantic and heights[curr_i][curr_j-1] >= heights[curr_i][curr_j]:
            kolejka__atlantic.append((curr_i,curr_j-1))
            visited_atlantic.add((curr_i,curr_j-1))
    return list(visited_pacific & visited_atlantic)