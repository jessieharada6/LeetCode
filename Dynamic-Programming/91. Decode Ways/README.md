# 91.Decode Ways

https://leetcode.com/problems/decode-ways/

The base case of dp[0] is 1, because we need to consider for the initial elements being a pair
It is a similar problem to Fibonacci number,
except that we need to consider the boundaries:
For the single digit, it should be within [1, 9],
For the double digits, it should be within [10, 26],
For the leading 0, the dp[1] should be 0
