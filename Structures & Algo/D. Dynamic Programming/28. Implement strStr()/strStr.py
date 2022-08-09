#  O((n−m)*m)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        
        for i in range(m - n + 1):
            j = 0
            for j in range(n):
                if haystack[i + j] != needle[j]:
                    print("break")
                    j = -1
                    break
            if j == n - 1:
                return i
        
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        
        for i in range(m - n + 1):
            a = i
            b = 0
            while b < n and haystack[a] == needle[b]:
                a += 1
                b += 1
            if b == n:
                return i
        
        return -1


# kmp

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        
        dp = [[0] * 256 for _ in range(n)]
        dp[0][ord(needle[0])] = 1
        x = 0
        
        for i in range(1, n):
            for j in range(256):
                if ord(needle[i]) == j:
                    dp[i][j] = i + 1
                else:
                    dp[i][j] = dp[x][j]
            x = dp[x][ord(needle[i])]
        
        state = 0
        for i in range(m):
            state = dp[state][ord(haystack[i])]
            if state == n:
                return i - n + 1
        
        return -1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        
        # get states 
        dp = [[0] * 256 for _ in range(n)]
        dp[0][ord(needle[0])] = 1
        
        x = 0
        for j in range(1, n):
            for c in range(256):
                if ord(needle[j]) == c:
                    dp[j][c] = j + 1
                else:
                    dp[j][c] = dp[x][c]
            
            print(x, j, needle[j])
            x = dp[x][ord(needle[j])]
            print(x)
        
        # match pattern to text
        j = 0
        for i in range(m):
            j = dp[j][ord(haystack[i])]
            if j == n: return i - n + 1
        
        return -1

        
        
            
            