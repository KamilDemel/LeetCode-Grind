def f(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    i = 0
    j = 0
    new_nums= []
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            new_nums.append(nums1[i])
            i += 1
        else:
            new_nums.append(nums2[j])
            j += 1
    while i < m:
        new_nums.append(nums1[i])
        i += 1
    while j < n:
        new_nums.append(nums2[j])
        j += 1
    k = len(new_nums)
    left = 0
    right = k - 1
    if k % 2 == 1:
        median = (left + right) // 2
        return new_nums[median]
    else:
        median = (left + right) // 2
        return (new_nums[median] + new_nums[median + 1]) / 2