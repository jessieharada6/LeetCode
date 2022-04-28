class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        index = {}
        sum = 0
        ans = 0
        
        for i in range(len(hours)):
            sum += 1 if hours[i] > 8 else -1
            
            if sum not in index:
                index[sum] = i
            
            if sum > 0:
                ans = max(ans, i + 1)
            else:
                if sum - 1 in index:
                    ans = max(ans, i - index[sum - 1])
        return ans
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        iMap = {}
        sum = 0
        output = 0
        
        for i in range(len(hours)):
            sum += 1 if hours[i] > 8 else -1
            
            if sum not in iMap:
                iMap[sum] = i
            
            # scenario 1: there's a positive number (tiring day > normal day)
            if sum > 0:
                output = max(output, i + 1)
            # scenario 2: find an interval for (tiring day > normal day)
            else: 
                if sum - 1 in iMap:
                    output = max(output, i - iMap[sum - 1])
    
        return output
            