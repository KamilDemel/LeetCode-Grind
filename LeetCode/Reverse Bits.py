def solution(n):
    bin_n = bin(n)[2:].zfill(32)
    new_bin = bin_n[::-1]
    wynik = int(new_bin, 2)
    return wynik