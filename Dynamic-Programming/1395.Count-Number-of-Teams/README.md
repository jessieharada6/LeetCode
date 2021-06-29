# 1395.Count Number of Teams

https://leetcode.com/problems/count-number-of-teams/

Using the example of [2,5,3,4,1],
Let's focus on one point at a time.
The one point is assumed to be the middle point of the three soldiers.

For example, let's look at 2

Count the value of left-less-than(l-) 2 and left-greater-than(l+) 2, as well as right-less-than(r-) 2 and right-greater-than(r+) 2.

We can omit the first the last element.
For tbe first element, the l+ and l- are 0.
For the last element, the r+ and r- are 0

Then, we sum all values by (l+ _ r-) + (l- _ r+)
