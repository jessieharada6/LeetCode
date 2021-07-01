# 322. Coin Change

https://leetcode.com/problems/coin-change/

Classic DP problem:
The base case is when the amount is 0, we take 0 coins.

```
we have coins of [1, 2, 5] and amount of 11
```

In order to work towards the goal of 11, we map out the values from 1 - 11.

| amount           | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| min num of coins | 0   | 1   | 1   | 2   | 2   | 1   | 2   | 2   | 3   | 3   | 2   | 3   |

We initiate the array with a large number, so that if we can't use the coins on hand to get to the number, we can return -1

At each amount, with coins on hand, if the current amount - current coin is greater than or equal to 0, we make a decision:
we either take the coin, 1 + dp[i - coin]
or we don't take the coin, dp[i]
because we have computed the previous values, we can get those values easily
