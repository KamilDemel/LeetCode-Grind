def sol(gas,cost):
    if sum(gas) < sum(cost):
        return -1
    curr_tank = 0
    start_idx = 0
    for i in range(len(gas)):
        curr_tank += (gas[i] - cost[i])
        if curr_tank < 0:
            start_idx = i + 1
            curr_tank = 0
    return start_idx