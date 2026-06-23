from collections import defaultdict
from collections import deque
class Node:
    def __init__(self,left=None,right=None ):
        self.left = left
        self.right = right
        self.x = None
def widentall(root):
    if not root:
        return 0
    poziomy = defaultdict(int)
    poziom = 0
    kolejka = deque()
    kolejka.append(root)
    poziomy[poziom] += 1
    poziom += 1
    while kolejka:
        for _ in range(len(kolejka)):
            curr_root = kolejka.popleft()
            if curr_root.right:
                kolejka.append(curr_root.right)
                poziomy[poziom] += 1
            if curr_root.left:
                kolejka.append(curr_root.left)
                poziomy[poziom] += 1
        poziom += 1
    najwieksza_szerokosc = max(poziomy.values())
    tab = []
    for a,b in poziomy.items():
        if b == najwieksza_szerokosc:
            tab.append(a)
    najwieksza_wysokosc = max(tab)
    def tnij_drzewo(node, poziom):
        if not node:
            return False, 0
        if poziom == najwieksza_wysokosc:
            ciecia = 0
            if node.left: ciecia += 1
            if node.right: ciecia += 1
            return True, ciecia
        lewy_dociera, lewe_ciecia = tnij_drzewo(node.left, poziom + 1)
        prawy_dociera, prawe_ciecia = tnij_drzewo(node.right, poziom + 1)
        moje_ciecia = 0
        ja_docieram = False
        if node.left:
            if lewy_dociera:
                moje_ciecia += lewe_ciecia
                ja_docieram = True
            else:
                moje_ciecia += 1
        if node.right:
            if prawy_dociera:
                moje_ciecia += prawe_ciecia
                ja_docieram = True
            else:
                moje_ciecia += 1
        return ja_docieram, moje_ciecia
    czy_korzen_dociera, calkowita_liczba_ciec = tnij_drzewo(root, 0)
    return calkowita_liczba_ciec

