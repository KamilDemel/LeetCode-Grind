def sol(triplets,target):
    curr_a = 0
    curr_b = 0
    curr_c = 0
    for i in range(len(triplets)):
        if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
            continue
        curr_a = max(curr_a,triplets[i][0])
        curr_b = max(curr_b, triplets[i][1])
        curr_c = max(curr_c, triplets[i][2])
    if curr_a == target[0] and curr_b == target[1] and curr_c == target[2]:
        return True
    return False