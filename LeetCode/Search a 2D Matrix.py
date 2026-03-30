def sol(matrix,target):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res.append(matrix[i][j])
    left = 0
    right = len(res) - 1
    while left <= right:
        mid = (left + right) // 2
        if res[mid] == target:
            return True
        elif res[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False
def sol_v2(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    left = 0
    right = (n * m) - 1
    while left <= right:
        mid = (left + right) // 2
        row = mid // m
        col = mid % m
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

