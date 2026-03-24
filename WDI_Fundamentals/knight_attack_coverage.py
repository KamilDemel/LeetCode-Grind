def find_most_valuable_knight_to_remove(knights_list, n):
    """
    Calculates which knight, if removed, would free up the most cells
    that are currently only attacked/occupied by that single knight.
    """
    board = [[0] * n for _ in range(n)]

    knight_moves = [
        (1, 2), (2, 1), (2, -1), (-1, 2),
        (-1, -2), (-2, -1), (-2, 1), (1, -2)
    ]
    for x, y in knights_list:
        board[x][y] += 1
        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] += 1

    max_cells_freed = 0

    for x, y in knights_list:
        cells_freed_by_this_knight = 0

        if board[x][y] == 1:
            cells_freed_by_this_knight += 1

        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1:
                    cells_freed_by_this_knight += 1

        if cells_freed_by_this_knight > max_cells_freed:
            max_cells_freed = cells_freed_by_this_knight

    return max_cells_freed
