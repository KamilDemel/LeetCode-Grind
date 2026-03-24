class Solution(object):
    def divide(self, dividend, divisor):
        is_negative = (dividend < 0) != (divisor < 0)
        ab_dividend = abs(dividend)
        abs_divisor_orig = abs(divisor)
        res = 0
        while ab_dividend >= abs_divisor_orig:
            ctr = 0
            temp_divisor = abs_divisor_orig
            while ab_dividend >= temp_divisor:
                temp_divisor = temp_divisor << 1
                ctr += 1
            temp_divisor = temp_divisor >> 1
            ab_dividend -= temp_divisor
            res += (1 << (ctr - 1))
        res = -res if is_negative else res
        INT_MIN, INT_MAX = -2147483648, 2147483647
        if res < INT_MIN: return INT_MIN
        if res > INT_MAX: return INT_MAX
        return res