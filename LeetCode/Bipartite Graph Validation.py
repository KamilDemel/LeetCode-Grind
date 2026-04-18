import collections
def solution(graf):
    kolory = [-1] * len(graf)
    for i in range(len(graf)):
        if kolory[i] == -1:
            kolejka = collections.deque()
            kolejka.append(i)
            kolory[i] = 0
            while kolejka:
                curr_i = kolejka.popleft()
                for k in range(len(graf[curr_i])):
                    if kolory[graf[curr_i][k]] == -1:
                        kolory[graf[curr_i][k]] = 1 - kolory[curr_i]
                        kolejka.append(graf[curr_i][k])
                    elif kolory[curr_i] == kolory[graf[curr_i][k]]:
                        return False
    return True