class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # true xor true = false (0)
        # false xor false = false (0)
        # true xor false = true (1)
        # false xor true = true (1)
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        output = 0
        
        # 19 / 3
        while divisor <= dividend:
            # temp is 3
            temp = divisor
            # 2 ^ mul
            mul = 1
            
            while dividend >= temp:
                # exit the outer while
                dividend -= temp
                # reaching the max
                output += mul
                
                # temp << 1 = 3 * 2 
                temp <<= 1
                mul <<= 1
            
                
        output *= sign
        
        return min(max(-2147483648, output), 2147483647)