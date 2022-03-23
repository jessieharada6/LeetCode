class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # (0, 1, 2)
        # arr = [2,3,1,6,7]
        # i = 0, j = 1, k = 2
        # 2 ^ 3 ^ 1 = 0
        # 1 ^ 6 ^ 7 = 0
        # as i < j <= k, 2 ways to divide the triplets as j can be the same as k
        # (0,1,2) 2 = 3 ^ 1
        # (0,2,2) -> index 0 to index 2  2 ^ 3 ^ 1 = 2 ^ 2
        
        ans = 0
        n = len(arr)
        
        for i in range(n):
            xor = arr[i]
            for j in range(i + 1, n):
                xor ^= arr[j]
                if xor == 0:
                    ans += (j - i)
        
        return ans



class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # if a == b -> a ^ b = 0
        
        ans = 0
        n = len(arr)
        
        prefix = [0 for i in range(n + 1)]
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        # print(prefix)
        
        for i in range(n - 1):
            for j in range(i + 1 , n):
                for k in range(j, n):  
                    if prefix[i] ^ prefix[j] == prefix[j] ^ prefix[k + 1]:
                        # print(i, j, k + 1, prefix[i], prefix[j], prefix[k + 1])
                        ans += 1    
        
        return ans
