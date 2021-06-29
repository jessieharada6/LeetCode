# 1277.Count Square Submatrices with All Ones

https://leetcode.com/problems/count-square-submatrices-with-all-ones/

Look at the example below with the code,

- When i and j is 0:
  the result accumulates the initial value, either 1 or 0
- When i and j is above 0, and the element itself is not 0:
  the result is accumulated based on the minimum value of its neighbours + the initial value

```
Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
```
