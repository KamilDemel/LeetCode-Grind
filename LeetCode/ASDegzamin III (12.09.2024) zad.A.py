import collections
def mykoryza(G,T,d):
    slownik_grzybow = {}
    visited = set()
    kolejka = collections.deque()
    for i in range(len(T)):
        kolejka.append((T[i],i))
        slownik_grzybow[i] = [T[i]]
        visited.add(T[i])
    while kolejka:
        curr_v, curr_idx = kolejka.popleft()
        for sasiad in G[curr_v]:
            if sasiad in visited:
                continue
            else:
                kolejka.append((sasiad,curr_idx))
                visited.add(sasiad)
                slownik_grzybow[curr_idx].append(sasiad)
    return len(slownik_grzybow[d])