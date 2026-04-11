def merge(left,right):
    L = 0
    R = 0
    new_list = []
    while L < len(left) and R < len(right):
        if left[L] < right[R]:
            new_list.append(left[L])
            L += 1
        else:
            new_list.append(right[R])
            R += 1
    while L < len(left):
        new_list.append(left[L])
        L += 1
    while R < len(right):
        new_list.append(right[R])
        R += 1
    return new_list
def merge_sort(T):
    if len(T) < 2:
        return T
    mid = len(T) // 2
    prawy_t = T[:mid]
    lewy_t = T[mid:]
    sorted_prawy = merge_sort(prawy_t)
    sorted_lewy = merge_sort(lewy_t)
    return merge(sorted_lewy,sorted_prawy)
def f(T):
    res = merge_sort(T)
    czy_spelnia = True
    for target in range(len(res)):
        if not czy_spelnia:
            return False
        left = 0
        right = len(res) - 1
        while left < right:
            if left == target:
                left += 1
                continue
            elif right == target:
                right -= 1
                continue
            sum = res[left] + res[right]
            if res[target] == sum:
                break
            elif res[target] > sum:
                left += 1
            else:
                right -= 1
        else:
            czy_spelnia = False
    return True
