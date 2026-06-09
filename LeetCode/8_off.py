import sys
def function(A,B,C,d):
    funkcja = A * (d**2) + B * d + C
    return funkcja
inputt = sys.stdin.read().split()
dane = iter(inputt)
P = int(next(dane))
n = int(next(dane))
A = int(next(dane))
B = int(next(dane))
C = int(next(dane))
lista_lisci = []
for _ in range(n):
    lista_lisci.append((int(next(dane)),int(next(dane))))
liczba_skokow = 0
start_lisc_idx = None
start_energia = None
lista_lisci.sort()
for start_idx, energia in lista_lisci:
    if start_idx == 0:
        start_lisc_idx = start_idx
        start_energia = energia
globalne_najlepsze = {0: start_energia}
aktualna_fala = {start_lisc_idx: start_energia}
pozycje_lisci = [lisc[0] for lisc in lista_lisci]
while aktualna_fala:
    liczba_skokow += 1
    nastepna_fala = {}
    for idx_start, max_energia in aktualna_fala.items():
        pozycja_startowa = pozycje_lisci[idx_start]
        d_meta = P - pozycja_startowa
        if max_energia >= function(A,B,C,d_meta):
            print(liczba_skokow)
            sys.exit(0)
        for i in range(idx_start + 1, len(lista_lisci)):
            cel_pozycja,cel_energia = lista_lisci[i]
            if cel_pozycja <= pozycja_startowa:
                continue
            d = cel_pozycja - pozycja_startowa
            koszt_skoku = function(A,B,C,d)
            if koszt_skoku > max_energia:
                break
            energa_po_wyladowaniu = max_energia - koszt_skoku + cel_energia
            if energa_po_wyladowaniu > globalne_najlepsze.get(cel_pozycja,-1):
                globalne_najlepsze[cel_pozycja] = energa_po_wyladowaniu
                nastepna_fala[i] = energa_po_wyladowaniu
    aktualna_fala = nastepna_fala
print(-1)
