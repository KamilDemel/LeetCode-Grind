def sol(T):
    T.sort(reverse=True)
    suma = 0
    for i in range(len(T)):
        if (T[i] - i) > 0:
            suma += (T[i] - i)
    return suma
