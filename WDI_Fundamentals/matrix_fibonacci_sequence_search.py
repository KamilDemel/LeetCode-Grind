def find_fib_sequence_in_matrix(matrix):
    n = len(matrix)

    fib_set = set()
    a, b = 0, 1
    for _ in range(100):
        fib_set.add(a)
        a, b = b, a + b

    for r in range(n):
        for c in range(n - 2):
            if matrix[r][c] in fib_set and matrix[r][c + 1] in fib_set:
                seq = [matrix[r][c], matrix[r][c + 1]]
                for k in range(c + 2, n):
                    if matrix[r][k] == seq[-1] + seq[-2]:
                        seq.append(matrix[r][k])
                    else:
                        break
                if len(seq) >= 3: return seq

            if matrix[r][c] in fib_set and matrix[r][c + 1] in fib_set:
                seq = [matrix[r][c], matrix[r][c + 1]]
                for k in range(c + 2, n):
                    if matrix[r][k] == seq[-2] - seq[-1]:
                        seq.append(matrix[r][k])
                    else:
                        break
                if len(seq) >= 3: return seq

    for c in range(n):
        for r in range(n - 2):
            if matrix[r][c] in fib_set and matrix[r + 1][c] in fib_set:
                seq = [matrix[r][c], matrix[r + 1][c]]
                for k in range(r + 2, n):
                    if matrix[k][c] == seq[-1] + seq[-2]:
                        seq.append(matrix[k][c])
                    else:
                        break
                if len(seq) >= 3: return seq

            if matrix[r][c] in fib_set and matrix[r + 1][c] in fib_set:
                seq = [matrix[r][c], matrix[r + 1][c]]
                for k in range(r + 2, n):
                    if matrix[k][c] == seq[-2] - seq[-1]:
                        seq.append(matrix[k][c])
                    else:
                        break
                if len(seq) >= 3: return seq

    return None