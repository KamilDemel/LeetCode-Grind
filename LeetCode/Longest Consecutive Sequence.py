def f(nums):
    if nums == []:
        return 0
    wyst = set(nums)
    max_len = 1
    for element in wyst:
        if element - 1 not in wyst:
            seq_len = 1
            liczba = element
            while liczba + 1 in wyst:
                seq_len += 1
                liczba += 1
            if seq_len > max_len:
                max_len = seq_len
    return max_len
