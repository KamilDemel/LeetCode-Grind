class Solution(object):
    def maxArea(self, height):
        """
        n = len(height)
        max_p = 0
        for i in range(n):
            for j in range(i+1,n):
                wys = min(height[i],height[j])
                szer = j - i
                p = wys * szer
                if p > max_p:
                    max_p = p
        return max_p
        """
        """
        n = len(height)
        max_p = 0
        left = 0
        for right in range(n):
            p = min(height[right],height[left]) * (right - left)
            while height[right] > height[left]:
                left += 1
            if p > max_p:
                max_p = p
        return max_p
        """
        n = len(height)
        max_p = 0
        left = 0
        right = n - 1
        while left < right:
            p = (right - left) * min(height[right],height[left])
            if p > max_p:
                max_p = p
            if height[right] > height[left]:
                left+=1
            else:
                right-=1
        return max_p