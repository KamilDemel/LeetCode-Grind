def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve_dual_rook_paths(matrix):
    n = len(matrix)

    def path_top_left(steps=0, r=0, c=0):
        if steps == 2 * n - 2:
            return r == n - 1 and c == n - 1

        if c + 1 < n and gcd(matrix[r][c], matrix[r][c + 1]) == 1:
            if path_top_left(steps + 1, r, c + 1):
                return True
        if r + 1 < n and gcd(matrix[r][c], matrix[r + 1][c]) == 1:
            if path_top_left(steps + 1, r + 1, c):
                return True
        return False

    def path_top_right(steps=0, r=0, c=n - 1):
        if steps == 2 * n - 2:
            return r == n - 1 and c == 0

        if c - 1 >= 0 and gcd(matrix[r][c], matrix[r][c - 1]) == 1:
            if path_top_right(steps + 1, r, c - 1):
                return True
        if r + 1 < n and gcd(matrix[r][c], matrix[r + 1][c]) == 1:
            if path_top_right(steps + 1, r + 1, c):
                return True
        return False

    res1 = path_top_left()
    res2 = path_top_right()

    if res1 and not res2:
        return 1
    elif not res1 and res2:
        return 2
    elif res1 and res2:
        return 3
    return 0