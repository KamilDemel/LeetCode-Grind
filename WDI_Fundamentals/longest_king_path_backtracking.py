def find_longest_king_path(N, obstacles):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    for obs in obstacles:
        row, col = obs[0], obs[1]
        grid[row][col] = 1

    def solve(r=0, c=0, distance=0):
        if r == N - 1 and c == N - 1:
            return distance

        max_dist = None
        grid[r][c] = 1
        directions = [(r + 1, c), (r, c + 1), (r - 1, c)]

        for next_r, next_c in directions:
            if 0 <= next_r < N and 0 <= next_c < N and grid[next_r][next_c] != 1:
                res = solve(next_r, next_c, distance + 1)
                if res is not None:
                    if max_dist is None or res > max_dist:
                        max_dist = res
        grid[r][c] = 0
        return max_dist

    return solve()