class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l, r = 0, n - k
        
        while l <= r:
            m = (l + r) // 2
            if m + k >= n:
                break
            if x - arr[m] <= arr[m + k] - x:
                r = m - 1
            else:
                l = m + 1
        
        return arr[l:l + k]

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        l, r = 0, n - 1 
        while l <= r:
            m = (l + r) // 2
            if arr[m] < x:
                l = m + 1
            else:
                r = m - 1
        
        o = 0
        if l >= n:
            o = r
        if r < 0:
            o = l
        
        if l < n and r >= 0:
            if abs(arr[l] - x) < abs(arr[r] - x):
                o = l
            else:
                o = r
        
        s, e = max(o - k + 1, 0), min(o + k - 1, n - 1)
        while e - s + 1 > k:
            if abs(arr[s] - x) <= abs(arr[e] - x):
                e -= 1
            else: 
                s += 1

        return arr[s:e + 1]       


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        start, end = 0, n - 1
        while end - start + 1 != k:
            if abs(arr[end] - x)  < abs(arr[start] - x):
                start += 1
            else:
                end -= 1

        return arr[start:end + 1]
