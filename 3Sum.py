def f(nums):
    nums.sort()
    n = len(nums)
    wynik = []
    for i in range(n):
        x = nums[i]
        if x > 0:
            break
        if i > 0 and x == nums[i-1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            if nums[left] + nums[right] + x == 0:
                y = nums[left]
                wynik.append([nums[right],nums[left],x])
                left += 1
                while left < right and y == nums[left]:
                    left += 1
            elif nums[left] + nums[right] + x > 0:
                right -= 1
            else:
                left += 1
    return wynik
