# 70. Climbing Stairs

https://leetcode.com/problems/climbing-stairs/

0 and 1 are the base case
| stairs | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| distinct ways | 1 | 1 | 2 | 3 | 5 | 8 |

ways[i] = stairs[i - 1] + stairs[i - 2]
