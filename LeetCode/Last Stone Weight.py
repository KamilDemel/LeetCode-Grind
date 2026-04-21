import heapq
def solution(stones):
    for i in range(len(stones)):
        stones[i] = -stones[i]
    heapq.heapify(stones)
    while stones and len(stones) != 1:
        y = heapq.heappop(stones)
        x = heapq.heappop(stones)
        if x != y:
            heapq.heappush(stones,-((-y) - (-x)))
    if len(stones) == 1:
        return -stones[0]
    else:
        return 0