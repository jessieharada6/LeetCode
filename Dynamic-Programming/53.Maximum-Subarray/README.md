# 53.Maximum Subarray

https://leetcode.com/problems/maximum-subarray/

Given the array of [-2,1,-3,4,-1,2,1,-5,4], at first, we may try to think in the greedy way, however, the trick is to focus on one element at a time.

**How**
Let's start with -2, which is the first element.
The option is to select this element as our current max.
Let's then move onto 1, which is the second element.
We have two options, we either select 1, or we sum 1 with -2 = -1, between 1, and -1, we select 1, and this has become our Current max,

| nums       | -2  | 1   | -3  | 4   | -1  | 2   | 1   | -5  | 4   |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| currentMax | -2  | 1   | -2  | 4   | 3   | 5   | 6   | 1   | 5   |
| max        | -2  | 1   | -2  | 4   | 4   | 5   | 6   | 6   | 6   |
