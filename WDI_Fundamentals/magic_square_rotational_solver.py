def rotate_row_right(matrix, row_idx):
    n = len(matrix)
    last_val = matrix[row_idx][n - 1]
    for i in range(n - 1, 0, -1):
        matrix[row_idx][i] = matrix[row_idx][i - 1]
    matrix[row_idx][0] = last_val
    return matrix


def rotate_col_down(matrix, col_idx):
    n = len(matrix)
    last_val = matrix[n - 1][col_idx]
    for i in range(n - 1, 0, -1):
        matrix[i][col_idx] = matrix[i - 1][col_idx]
    matrix[0][col_idx] = last_val
    return matrix


def is_magic_square(matrix):
    n = len(matrix)
    target_sum = sum(matrix[0])

    for i in range(n):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j][i] for j in range(n))

        if row_sum != target_sum or col_sum != target_sum:
            return False

    return True


def deep_copy(matrix):
    return [row[:] for row in matrix]


def can_become_magic(matrix):
    n = len(matrix)
    limit = 2 * n

    for move1 in range(limit):
        for move2 in range(limit):
            temp_matrix = deep_copy(matrix)

            if move1 < n:
                rotate_row_right(temp_matrix, move1)
            else:
                rotate_col_down(temp_matrix, move1 - n)

            if move2 < n:
                rotate_row_right(temp_matrix, move2)
            else:
                rotate_col_down(temp_matrix, move2 - n)

            if is_magic_square(temp_matrix):
                return True

    return False