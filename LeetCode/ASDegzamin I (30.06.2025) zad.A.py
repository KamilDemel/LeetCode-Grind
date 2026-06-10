def battle(P,K,R):
    lista = []
    n = len(K)
    m = len(P)
    max_zakres_idx = ((4 * n) + (4 * m)) + 1
    tablica_counting = [0] * max_zakres_idx
    for pozycja_kataapulty, zasieg in zip(K,R):
        lista.append((pozycja_kataapulty,zasieg))
    for pozycja_procesora in P:
        lista.append((pozycja_procesora,0))
    slownik_idx = {}
    for index, (pozycja, zasieg) in enumerate(lista):
        slownik_idx[pozycja] = zasieg
    listaa_katapult = []
    for a,b in lista:
        listaa_katapult.append(a)
    for i in range(len(listaa_katapult)):
        tablica_counting[listaa_katapult[i]] = 1
    posortowania_lista = []
    for i in range(len(tablica_counting)):
        if tablica_counting[i] == 1:
            posortowania_lista.append(i)
    tablica_finish = []
    for i in range(len(posortowania_lista)):
        tablica_finish.append([posortowania_lista[i],slownik_idx[posortowania_lista[i]]])
    licznik = 0
    for i in range(len(tablica_finish)):
        pozycja_procesoraa,zasieg = tablica_finish[i]
        if zasieg > 0:
            continue
        for j in range(i-1, -1,-1):
            if tablica_finish[j][1] > 0:
                if (pozycja_procesoraa - tablica_finish[j][0]) <= tablica_finish[j][1]:
                    licznik += 1
                    tablica_finish[j][1] = -1
                    break
    return licznik

