import random

def perform_test(N):
    T = [0] * N
    def fill(T, N):
        for k in range(N):
            T[k] = random.randint(1, 365)
    fill(T, N)
    occurrences = [0] * 366
    for i in range(N):
        occurrences[T[i]] += 1
    for count in occurrences:
        if count >= 2:
            return True
    return False

trial_count = 1000
for N in range(20, 41):
    total = 0
    for _ in range(trial_count):
        if perform_test(N):
            total += 1
    print(f"Number of people: {N} Experiment result: {total/trial_count}")