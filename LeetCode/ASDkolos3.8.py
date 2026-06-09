def min_cost( O, C, T, L):
    lista = [(0,0),(25,0)]
    for a,b in zip(O,C):
        lista.append((a,b))
    lista.sort(key=lambda item:item[0])
    dp_bez_sup_skoku = [float("inf")] * (len(O) + 2)
    dp_z_sup_skokiem = [float("inf")] * (len(O) + 2)
    dp_bez_sup_skoku[0] = 0
    dp_z_sup_skokiem[0] = 0
    for i in range(1, len(lista)):
        for j in range(0,i):
            if T < lista[i][0] - lista[j][0] <= 2 * T:
                dp_z_sup_skokiem[i] = min(dp_bez_sup_skoku[j] + lista[i][1],dp_z_sup_skokiem[i])
            if lista[i][0] - lista[j][0] <= T:
                dp_bez_sup_skoku[i] = min(dp_bez_sup_skoku[j] + lista[i][1],dp_bez_sup_skoku[i])
                dp_z_sup_skokiem[i] = min(dp_z_sup_skokiem[j] + lista[i][1], dp_z_sup_skokiem[i])
    wynik = min(dp_z_sup_skokiem[-1],dp_bez_sup_skoku[-1])
    return wynik
