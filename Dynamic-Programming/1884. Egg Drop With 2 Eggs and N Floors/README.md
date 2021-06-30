# 1884. Egg Drop With 2 Eggs and N Floors

https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

| count | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| i     | 1   | 2   | 2   | 3   | 3   | 3   | 3   | 4   | 4   | 4   | 4   | 5   | 5   | 5   | 5   |

https://www.mathsisfun.com/algebra/triangular-numbers.html
Now it is easy to work out how many dots: just multiply n by n+1
Dots in rectangle = n(n+1)
But remember we doubled the number of dots, so
Dots in triangle = n(n+1)/2

Egg 1 is to determine the range
10 19 28
Egg 2 is to determine the exact floor based on the range
[1, 9], [11, 18], [20, 27]
x + (x - 1) + (x - 2) + ... = 100
