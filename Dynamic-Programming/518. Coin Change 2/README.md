# 518. Coin Change 2

https://leetcode.com/problems/coin-change-2/

| amount    | 0   | 1   | 2   | 3   | 4   | 5   |
| --------- | --- | --- | --- | --- | --- | --- |
| [1]       | 1   | 1   | 1   | 1   | 1   | 1   |
| [1, 2]    | 1   | 1   | 2   | 2   | 3   | 3   |
| [1, 2, 5] | 1   | 1   | 1   | 1   | 1   | 4   |

base case is dp[0] = 1 as shown above
then based on each coin amount, as long as the current amount - coin amount >= 0
we have two options, we choose or not choose
The array is therefore updated
