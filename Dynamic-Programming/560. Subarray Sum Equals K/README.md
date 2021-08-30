# 560. Subarray Sum Equals K

https://leetcode.com/problems/subarray-sum-equals-k/

[1, 2, 1, 3] and k = 3
*** sum = k
[1, 3, 4, 7]
4 - 1 = k, 7 - 4 = k
3 at the second index as sum is k itself
3 - 0 = k
so we need map.set(0, 1)