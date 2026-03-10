class Solution:
    def sortArray(self, nums):
        def merge(left,right):
            R = 0
            L = 0
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
            if len(T) <= 1:
                return T
            mid = len(T) // 2
            left_tab = T[:mid]
            right_tab = T[mid:]
            sort_left = merge_sort(left_tab)
            sort_right = merge_sort(right_tab)
            return merge(sort_left, sort_right)
        return merge_sort(nums)