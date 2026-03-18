def f(numbers, target):
    n = len(numbers)
    left = 0
    right = n - 1
    wynik = []
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            wynik.append(left+1)
            wynik.append(right+1)
            return wynik
        elif sum > target:
            right -= 1
        else:
            left += 1
    return wynik