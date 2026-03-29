def brute_solution(temperatures):
    n = len(temperatures)
    res = []
    for i in range(n):
        ctr = 0
        for j in range(i+1,n):
            if temperatures[j] > temperatures[i]:
                ctr+=1
                break
            ctr += 1
        else:
            ctr = 0
        res.append(ctr)
    return res
def solution(temperatures):
    n = len(temperatures)
    stos = []
    res = [0] * n
    for i in range(n):
        while stos and temperatures[i] > temperatures[stos[-1]]:
            wynik = stos.pop()
            res[wynik] += i - wynik
        stos.append(i)
    return res