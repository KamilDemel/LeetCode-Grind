def add_element(tab,val):
    tab.append(val)
    i = len(tab) - 1
    idx_parent = (i - 1) // 2
    while i > 0 and tab[idx_parent] < tab[i]:
        tab[i],tab[idx_parent] = tab[idx_parent],tab[i]
        i = idx_parent
        idx_parent = (i-1) // 2
    return tab
