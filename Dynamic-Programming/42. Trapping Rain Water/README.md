# 42. Trapping Rain Water

https://leetcode.com/problems/trapping-rain-water/

| height                | 0   | 1   | 0   | 2   | 1   | 0   | 1   | 3   | 2   | 1   | 2   | 1   |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| maxLeft               | 0   | 0   | 1   | 1   | 2   | 2   | 2   | 2   | 3   | 3   | 3   | 3   |
| maxRight              | 3   | 3   | 3   | 3   | 3   | 3   | 3   | 2   | 2   | 2   | 1   | 0   |
| min(L, R)             | 0   | 0   | 1   | 1   | 2   | 2   | 2   | 2   | 2   | 2   | 1   | 0   |
| min(L, R) - height[i] | 0   | -1  | 1   | -1  | 1   | 2   | 1   | -1  | 0   | 1   | -1  | -1  |

sum = 1 + 1 + 2 + 1 + 1

formula: Math.min(maxL, maxR) - height[i]

move the L pointer to the current value, then get maxL, sum it using the formula above
move the R pointer to the current value, then get maxR, sum it using the formula above

Useful link: https://www.youtube.com/watch?v=ZI2z5pq0TqA
