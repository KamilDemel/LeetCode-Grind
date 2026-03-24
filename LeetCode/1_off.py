import sys
from random import randint, seed

OIOIOI = True


def solution(T):
    if not T:
        return 0

    unique_sorted = sorted(list(set(T)))
    ranks = {word: i + 1 for i, word in enumerate(unique_sorted)}

    max_rank = len(unique_sorted)
    bit = [0] * (max_rank + 1)

    def add(idx, val):
        while idx <= max_rank:
            bit[idx] += val
            idx += idx & (-idx)

    def query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s

    max_domi = 0
    for word in T:
        rank = ranks[word]
        count_smaller = query(rank - 1)
        if count_smaller > max_domi:
            max_domi = count_smaller
        add(rank, 1)

    return max_domi
if __name__ == "__main__":
    def generate_random_string(length):
        return ''.join(chr(randint(97, 122)) for _ in range(length))


    if OIOIOI:
        n = int(sys.stdin.readline().strip())
        words = [sys.stdin.readline().strip() for _ in range(n)]
        print(solution(words))
    else:
        seed(1)
        test_def = [
            (10, 5, 10, 6),
            (100, 5, 10, 88),
            (100, 20, 100, 91),
            (10000, 10, 30, 9901)
        ]
        ok = 0
        for idx, (n, m_low, m_high, ans) in enumerate(test_def):
            print("Test", idx + 1)
            words = [generate_random_string(randint(m_low, m_high)) for _ in range(n)]
            result = solution(words)
            if result == ans:
                print("OK")
                ok += 1
            else:
                print("Błąd!")
                print(f"Oczekiwane: {ans}, Zwrócone: {result}")
        print("Wynik:", ok, "/", len(test_def))



