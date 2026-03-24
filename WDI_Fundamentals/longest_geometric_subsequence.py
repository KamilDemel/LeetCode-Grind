def get_longest_geometric_subsequence(T, N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    max_length = 2
    current_length = 2
    for i in range(2, N):
        a = T[i - 2]
        b = T[i - 1]
        c = T[i]
        if b ** 2 == a * c and (b != 0 or c == 0):
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 2
    return max_length