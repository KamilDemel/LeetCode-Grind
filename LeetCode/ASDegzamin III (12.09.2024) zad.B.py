def kunlucky(T,k):
    first = k
    liczby_k_pechowe = set()
    liczby_k_pechowe.add(k)
    for i in range(1,len(T)):
        liczba = first + (first % i) + 7
        if liczba > len(T):
            break
        liczby_k_pechowe.add(liczba)
        first = liczba
    left = 0
    ctr_pechowych = 0
    best_dl = 0
    for right in range(len(T)):
        if T[right] in liczby_k_pechowe:
            ctr_pechowych += 1
        while ctr_pechowych > 2:
            if T[left] in liczby_k_pechowe:
                ctr_pechowych -= 1
            left += 1
        if right - left + 1 > best_dl:
            best_dl = right - left + 1
    return best_dl


