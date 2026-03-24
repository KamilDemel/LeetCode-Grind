def solve_thirteen(T):
    N = len(T)

    def rek_pomoc(i=0, licznik=0, suma_pol=0, wybrane=None):
        if wybrane is None:
            wybrane = []

        if licznik == 13 and suma_pol == 2024:
            return True

        if i == N:
            return False

        x1, x2, y1, y2 = T[i]
        czy_biore = True

        for j in range(len(wybrane)):
            x3, x4, y3, y4 = wybrane[j]
            sa_rozlaczne = (x2 < x3 or x1 > x4 or y2 < y3 or y1 > y4)
            if not sa_rozlaczne:
                czy_biore = False
                break

        if czy_biore:
            pole = abs(x2 - x1) * abs(x2 - x1)
            if rek_pomoc(i + 1, licznik + 1, suma_pol + pole, wybrane + [T[i]]):
                return True

        if rek_pomoc(i + 1, licznik, suma_pol, wybrane):
            return True

        return False

    return rek_pomoc()