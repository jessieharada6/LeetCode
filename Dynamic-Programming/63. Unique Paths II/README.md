# 63. Unique Paths II

https://leetcode.com/problems/unique-paths-ii/

```
Example: [
    [0,0,0],
    [0,1,0],
    [0,0,0]]
```

The updated dp:
[ 1, 1, 1 ]
[ 1, 0, 1 ]
[ 1, 1, 2 ]

2 is based on initial value (at the second row) + the updated dp[i - 1]

