class Solution(object):
    def romanToInt(self, s):
        num_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        dl = len(s)

        """
        prev = num_dict[s[0]]
        for num in range(1,dl):
            curr = num_dict[s[num]]
            sum += curr
            if curr > prev:
                sum -= 2 * prev
            prev = curr
        sum += num_dict[s[0]]
        return sum
        """

        prev = -1
        sum2 = 0
        for num in range(dl-1,-1,-1):
            curr = num_dict[s[num]]
            if curr >= prev:
                sum2 += curr
            else:
                sum2 -= curr
            prev = curr
        return sum2