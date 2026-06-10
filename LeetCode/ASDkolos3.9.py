p = True
c = False
P = [(1,c),(3,c),(4,c),(6,c),(8,c),(9,c),(11,c),(13,c),(16,c),(17,c),
(2,p),(5,p),(7,p),(10,p),(12,p),(14,p),(15,p),(18,p)]
B = 20
mapa_indeksow = {}
for indeks, (x, rodzaj) in enumerate(P):
    mapa_indeksow[x] = indeks
os_kontrolne = [0] * (B + 1)
for x, is_przesiadka in P:
    if not is_przesiadka:
        os_kontrolne[x] = 1
pref_kontrolne = [0] * (B + 1)
for k in range(1, B + 1):
    pref_kontrolne[k] = pref_kontrolne[k-1] + os_kontrolne[k]
lista_przesiadkowych = [0]
P.sort(key=lambda item:item[0])
for a,b in P:
    if b:
        lista_przesiadkowych.append(a)
lista_przesiadkowych.append(B)
N = len(lista_przesiadkowych)
dp_jacek = [float("inf")] * N
dp_marian = [float("inf")] * N
dp_jacek[0] = 0
dp_marian[0] = 0
poprzednik_marian = [0] * N
poprzednik_jacek = [0] * N
for i in range(1,N):
    for skok in range(1,4):
        j = i - skok
        if j < 0:
            break
        pozycja_i = lista_przesiadkowych[i]
        pozycja_j = lista_przesiadkowych[j]
        koszt = pref_kontrolne[pozycja_i] - pref_kontrolne[pozycja_j]
        nowy_koszt_mariana = dp_jacek[j] + koszt
        if nowy_koszt_mariana < dp_marian[i]:
            dp_marian[i] = nowy_koszt_mariana
            poprzednik_marian[i] = j
        nowy_koszt_jacka = dp_marian[j] + 0
        if nowy_koszt_jacka < dp_jacek[i]:
            dp_jacek[i] = nowy_koszt_jacka
            poprzednik_jacek[i] = j
sciezka_x = []
if dp_marian[-1] <= dp_jacek[-1]:
    kto_oddaje = "marian"
else:
    kto_oddaje = "jacek"
obecny_indeks = N - 1
while obecny_indeks > 0:
    if kto_oddaje == "marian":
        poprzedni = poprzednik_marian[obecny_indeks]
        kto_oddaje = "jacek"
    else:
        poprzedni = poprzednik_jacek[obecny_indeks]
        kto_oddaje = "marian"
    if poprzedni > 0:
        wspolrzedna = lista_przesiadkowych[poprzedni]
        sciezka_x.append(wspolrzedna)
    obecny_indeks = poprzedni
sciezka_x.reverse()
wynik = [mapa_indeksow[x] for x in sciezka_x]
print(wynik)
