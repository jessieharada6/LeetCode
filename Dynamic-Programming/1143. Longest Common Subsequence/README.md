# 1143. Longest Common Subsequence

https://leetcode.com/problems/longest-common-subsequence/

Bottom up approach

| text2/text1 | a   | c   | e                  | ""  |
| ----------- | --- | --- | ------------------ | --- |
| a           | 3   | 2   | 1                  | 0   |
| b           | 2   | 2   | 1                  | 0   |
| c           | 2   | 2   | 1                  | 0   |
| d           | 1   | 1   | 1                  | 0   |
| e           | 1   | 1   | 1 (starting point) | 0   |
|             | 0   | 0   | 0                  | 0   |

if characters are a match:
1 + dp[i + 1][j + 1] (diagnally - meaning see the remaining of the substring)
else:
max(dp[i + 1][j], dp[i][j + 1])

useful link:https://www.youtube.com/watch?v=Ua0GhsJSlWM
