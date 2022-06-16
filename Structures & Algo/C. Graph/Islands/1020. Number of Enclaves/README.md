# 1020. Number of Enclaves

https://leetcode.com/problems/number-of-enclaves/

work with union find too, union the edge 1's with dummy, then union the inner 1's with the same parent, then return the count the inner 1's in range of (1, m - 1)(1, n - 1)