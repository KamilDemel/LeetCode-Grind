def solution(colors):
    left = 0
    right = -1
    best_diff = 0
    best_diff_2 = 0
    for i in range(len(colors)-1,-1,-1):
        if colors[left] != colors[i]:
            best_diff = abs(i - left)
            break
    for j in range(len(colors)):
        if colors[right] != colors[j]:
            best_diff_2 = abs(j - (len(colors)-1))
            break
    return max(best_diff,best_diff_2)