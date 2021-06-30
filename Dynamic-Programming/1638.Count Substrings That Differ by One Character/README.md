# 1638. Count Substrings That Differ by One Character

https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

```
s = "aba", t = "baba"
```

Pick a starting point at s and t respectively, the length of the string is determined by the current comparing point. For example, if we let t be the inner loop, and we focus on a (t[1]), then the longest string would be "aba". i.e., pos + i < s.length && pos + j < t.length, at inner loop, pos stops when the moving index pos + j has reached the length of t.

As long as we found one difference, we can stop the current comparisons, because we only need to find the substring that has one different character. For example, when t is at t[0], "b", we compare "b" with s[0], which has one difference, at this point, we can stop.

It is not to compare every single character individually, but the substrings.
For example, when t is at t[2], "b", we compare "b" with "a" (i.e. s[0]), it is of one difference, then we continue with t[2] and t[3] - "ba", with s[0] and s[1], "ab", now the difference is more than one, so we stop.
Another example is that if the substring of s is "ab", and the subsrtring of t is "bb", we compare "b" (t[0]) with "a" (s[0]), there is one difference, then we carry the difference and continue to compare "bb" (t[0] and t[1]) with "ab" (s[0] and s[1]), the difference is still one. The point here is that we actually compared the substrings, rather than the individual character.
