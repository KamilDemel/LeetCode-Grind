def sol(intervals):
    intervals.sort()
    res = [intervals[0]]
    if len(intervals) == 1:
        return intervals
    for interval in intervals[1:]:
        if interval[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], interval[1])
            continue
        res.append(interval)
    return res



