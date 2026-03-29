import sys
def solve_brute():
    n, T = map(int, input().split())
    k = [0] * T
    for _ in range(n):
        a,b = map(int,input().split())
        for j in range(a,b+1):
            k[j] += 1
    maxx = max(k)
    for i in range(len(k)):
        if k[i] == maxx:
            print(maxx,i)
            break
def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    events = []
    for i in range(2,2*n+1,2):
        a = int(input_data[i])
        b = int(input_data[i+1])
        events.append((a,1))
        events.append((b+1,-1))
    events.sort()
    max_grubosc = 0
    akt_grubosc = 0
    best_i = None
    for km, grubosc in events:
        akt_grubosc += grubosc
        if akt_grubosc > max_grubosc:
            max_grubosc = akt_grubosc
            best_i = km
    print(max_grubosc,best_i)
if __name__ == "__main__":
    #solve_brute()
    solve()