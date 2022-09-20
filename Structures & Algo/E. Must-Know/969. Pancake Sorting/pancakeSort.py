class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
    
        def reverse(n):
            if n == 1: return

            max_idx = 0
            max_val = 0
            for i in range(n):
                if arr[i] > max_val:
                    max_val = arr[i]
                    max_idx = i

            sort(0, max_idx)
            sort(0, n - 1)

            res.append(max_idx + 1)
            res.append(n)
            
            reverse(n - 1)
            

        def sort(i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        reverse(len(arr))
        return res


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if not arr: 
            return []
        
        res = []
        idx = arr.index(max(arr))
        arr = arr[:idx + 1][::-1] + arr[idx + 1:]
        arr = arr[::-1]
        res += [idx + 1, len(arr)]
        
        temp = self.pancakeSort(arr[:-1])
        res += temp
        return res
        
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        
        while n > 0:
            idx = arr.index(max(arr[:n]))
            arr = arr[:idx + 1][::-1] + arr[idx + 1:]
            arr = arr[:n][::-1]
            res += [idx + 1, n]
            n -= 1
        
        return res