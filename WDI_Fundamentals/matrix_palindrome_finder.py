def is_palindrome(text, start, end):
    left = start
    right = end
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


def get_length(text):
    count = 0
    for _ in text:
        count += 1
    return count


def get_column(grid, col_idx):
    result = ""
    for i in range(get_length(grid)):
        result += grid[i][col_idx]
    return result


def get_diagonal_lr(grid, r, c):
    length = get_length(grid)
    result = ""
    while r < length and c < length:
        result += grid[r][c]
        r += 1
        c += 1
    return result


def get_diagonal_rl(grid, r, c):
    length = get_length(grid)
    result = ""
    while r < length and c >= 0:
        result += grid[r][c]
        r += 1
        c -= 1
    return result


def search_in_text(text, found_list):
    length = get_length(text)
    for start in range(length):
        for end in range(start + 4, length):
            if is_palindrome(text, start, end):
                found_word = ""
                for k in range(start, end + 1):
                    found_word += text[k]

                if found_word in found_list:
                    return found_word
                else:
                    found_list += [found_word]
    return None


def solve(grid, n):
    found = []

    for row in grid:
        result = search_in_text(row, found)
        if result is not None:
            return result

    for j in range(n):
        col_text = get_column(grid, j)
        result = search_in_text(col_text, found)
        if result is not None:
            return result

    for k in range(n):
        diag_text = get_diagonal_lr(grid, 0, k)
        result = search_in_text(diag_text, found)
        if result is not None:
            return result

    for w in range(1, n):
        diag_text = get_diagonal_lr(grid, w, 0)
        result = search_in_text(diag_text, found)
        if result is not None:
            return result

    for k in range(n):
        diag_text = get_diagonal_rl(grid, 0, k)
        result = search_in_text(diag_text, found)
        if result is not None:
            return result

    for w in range(1, n):
        diag_text = get_diagonal_rl(grid, w, n - 1)
        result = search_in_text(diag_text, found)
        if result is not None:
            return result

    return None
