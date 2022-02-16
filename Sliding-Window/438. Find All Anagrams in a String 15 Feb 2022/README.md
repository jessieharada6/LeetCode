# 438. Find All Anagrams in a String

https://leetcode.com/problems/find-all-anagrams-in-a-string/

- use sliding window to avoid repeatingly building the hashMap of the longer string
- spit out a character from the left, and pop it if the value is 0
- add in the chracter from the right, position the right index at the targeted position to avoid index out of rangeA