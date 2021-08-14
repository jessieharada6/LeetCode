# 91.Decode Ways

https://leetcode.com/problems/decode-ways/

The base case of dp[0] is 1, because we need to consider for the initial elements being a pair
It is a similar problem to Fibonacci number,
except that we need to consider the boundaries:
For the single digit, it should be within [1, 9],
For the double digits, it should be within [10, 26],
For the leading 0, the dp[1] should be 0

"226"
dp 1, 1, 2, 3

dp[0] = 1 as base case
for example, 22 is valid, and we will add the number

dp[1] = 1 if s[0] != "0" else dp[1] = 0

then dp starts from the second index, for "226", starts at "6" (index 2)
then option1 is 2, option2 is 22 
then option1 is 6, option2 is 26
if option1 is valid, dp[i] += dp[i - 1]
if option2 is valid, dp[i] += dp[i - 2]"
