import sys
import array
def solution():
    dane = (x for line in sys.stdin for x in line.split())
    n = int(next(dane))
    T = array.array('i', (int(next(dane)) for _ in range(n)))
    q = int(next(dane))
    T = sorted(T, reverse=True)
    for i in range(1,q+1):
        szukana = int(next(dane))
        sys.stdout.write(str(T[szukana - 1])+"\n")
if __name__ == "__main__":
    solution()
