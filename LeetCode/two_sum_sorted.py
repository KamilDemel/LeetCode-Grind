def two_sum(A,target):
    n = len(A)
    left = 0
    right = n - 1
    while left < right:
        suma = A[left] + A[right]
        if suma == target:
            return True
        elif suma > target:
            right -= 1
        else:
            left += 1
    return False