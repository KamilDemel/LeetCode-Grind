def solve_interval_sum(intervals, target_sum=2022):
    n = len(intervals)

    def backtrack(index, current_sum, selected_intervals):
        if current_sum == target_sum:
            return True

        if current_sum > target_sum or index == n:
            return False

        x1, y1 = min(intervals[index]), max(intervals[index])

        is_disjoint = True
        for x2, y2 in selected_intervals:
            if not (y1 < x2 or x1 > y2):
                is_disjoint = False
                break

        if is_disjoint:
            interval_length = abs(x1 - y1)
            if backtrack(index + 1, current_sum + interval_length, selected_intervals + [(x1, y1)]):
                return True

        if backtrack(index + 1, current_sum, selected_intervals):
            return True

        return False

    return backtrack(0, 0, [])
