# 62. Unique Paths

https://leetcode.com/problems/unique-paths/

Similar logic to 518. Coin Change 2, focus on the current coordinated, choose or not choose

base case is 1 for the first row and first column

| m     | 0   | 1   | 2   | 3   | 4   | 5   | 6   |
| ----- | --- | --- | --- | --- | --- | --- | --- |
| n = 0 | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
| n = 1 | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| n = 0 | 1   | 3   | 6   | 10  | 15  | 21  | 28  |
