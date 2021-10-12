# hash map
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        output = 0
        dict = collections.Counter(nums)
        # print(dict)
        
        for i in range(len(target)):
            prefix = target[0:i]
            suffix = target[i:len(target)]
            
            if prefix == suffix:
                output += dict[prefix] * (dict[suffix] - 1)
            else:
                output += dict[prefix] * dict[suffix]
        return output
        
                    
                

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq = Counter(nums)
        output = 0
        
        # freq
        # Counter({'77': 2, '777': 1, '7': 1}) 
        # freq.items()
        # dict_items([('777', 1), ('7', 1), ('77', 2)])
        
        for k, v in freq.items():
            # prefix target[0:len(k)]
            if target.startswith(k):
                suffix = target[len(k):]
                # print(target[0:len(k)], suffix, v, freq[suffix])
                output += v * freq[suffix]
                # prefix == suffix
                if k == suffix: 
                    output -= freq[suffix]
        return output
                    
                