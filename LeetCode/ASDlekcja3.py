def f(tab):
    n = len(tab)
    curr_min = float("inf")
    curr_max = float("-inf")
    for i in range(0,n-1,2):
        a, b = tab[i], tab[i+1]
        if a < b:
            if a < curr_min:
                curr_min = a
            if b > curr_max:
                curr_max = b
        else:
            if a > curr_max:
                curr_max = a
            if b < curr_min:
                curr_min = b
    if n % 2 == 1:
        if tab[-1] > curr_max:
            curr_max = tab[-1]
        if tab[-1] < curr_min:
            curr_min = tab[-1]
    return curr_min,curr_max