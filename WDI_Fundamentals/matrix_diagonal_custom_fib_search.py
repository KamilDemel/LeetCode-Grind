def find_custom_fib_diagonal(matrix):
    custom_fib = []
    a, b = 1, 2
    for _ in range(100):
        custom_fib.append(a)
        a, b = b, a + b - 1

    n = len(matrix)
    fib_len = len(custom_fib)

    for r in range(n):
        for c in range(n):
            for fib_idx in range(fib_len):
                if matrix[r][c] == custom_fib[fib_idx]:
                    match_count = 1

                    for k in range(1, n):
                        if (r + k < n and
                                c + k < n and
                                fib_idx + k < fib_len):

                            if custom_fib[fib_idx + k] == matrix[r + k][c + k]:
                                match_count += 1
                            else:
                                break
                        else:
                            break

                    if match_count >= 3:
                        return match_count
    return None