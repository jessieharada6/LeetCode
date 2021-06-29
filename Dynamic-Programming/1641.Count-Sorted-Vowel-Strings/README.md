# 1641.Count Sorted Vowel Strings
https://leetcode.com/problems/count-sorted-vowel-strings/

Let's look at the vowels from "u", "o", "i", "e", "a"
When n = 1, the strings consist of vowels 1, 1, 1, 1, 1
When n = 2, the strings consist of vowels 1, 2, 3, 4, 5
We can make a table as below:

| n   | 'u' | 'o' | 'i' | 'e' | 'a' |
| --- | --- | --- | --- | --- | --- |
| 1   | 1   | 1   | 1   | 1   | 1   |
| 2   | 1   | 2   | 3   | 4   | 5   |
| 3   | 1   | 3   | 6   | 10  | 15  |

Let's initiate an array of 5 elements, with base values of 1.

The updated dp[i] = the previous dp[i] + the updated dp[i - 1]

i.e., dp[i] = dp[i] + dp[i - 1]
