def tab_przecinajaca(nums,mid):
    lewy_max = float("-inf")
    obecna_suma = 0
    for i in range(mid-1, -1, -1):
        obecna_suma += nums[i]
        if obecna_suma > lewy_max:
            lewy_max = obecna_suma
    prawy_max = float("-inf")
    obecna_suma = 0
    for i in range(mid, len(nums)):
        obecna_suma += nums[i]
        if obecna_suma > prawy_max:
            prawy_max = obecna_suma
    opcja_c = lewy_max + prawy_max
    return opcja_c
def szukaj_sumy(T):
    if len(T) < 2:
        return T[0]
    mid = len(T) // 2
    left_tab = T[:mid]
    right_tab = T[mid:]
    lewa_suma = szukaj_sumy(left_tab)
    prawa_suma = szukaj_sumy(right_tab)
    przecinajaca_suma = tab_przecinajaca(T,mid)
    return max(lewa_suma,prawa_suma,przecinajaca_suma)
