def w_bin(tab):
    n = len(tab)
    r_prev = tab[1] - tab[0]
    left = 0
    right = n - 1
    ans = -1
    while left <= right:
        mid = (right + left) // 2
        p_value = tab[0] + (mid * r_prev)
        if tab[mid] == p_value:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
    return ans

