import heapq
def solution(points):
    suma = 0
    visited = set()
    start_point = 0
    pq = [(0,start_point)]
    while pq:
        curr_distance, curr_node = heapq.heappop(pq)
        if curr_node in visited:
            continue
        else:
            visited.add(curr_node)
            suma += curr_distance
            for next_node in range(len(points)):
                if next_node not in visited:
                    d = abs(points[curr_node][0] - points[next_node][0]) + abs(
                        points[curr_node][1] - points[next_node][1])
                    heapq.heappush(pq, (d, next_node))
    return suma