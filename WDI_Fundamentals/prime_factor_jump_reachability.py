def can_reach_end(T, N):
    reachable = [0] * N
    reachable[0] = 1
    for k in range(N):
        if reachable[k] == 1:
            divisor = 2
            current_field = T[k]
            while current_field > 1:
                if current_field % divisor == 0:
                    new_index = k + divisor
                    if new_index >= N:
                        break
                    else:
                        reachable[new_index] = 1
                        if reachable[-1] == 1:
                            return True
                    current_field = current_field // divisor
                else:
                    divisor += 1
    if reachable[-1] == 1:
        return True
    else:
        return False


