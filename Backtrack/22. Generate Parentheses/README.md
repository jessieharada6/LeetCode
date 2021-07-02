# 22. Generate Parentheses

https://leetcode.com/problems/generate-parentheses/

Useful link: https://www.youtube.com/watch?v=s9fokUqJ76A

base case: when open count and closed count are both equal to n, return
conditions:

1. open count < n, add "("
2. closed count < open count, add ")"
   essential to remove the current stack, so the current state (for example, "(("), remains at the current recursion state, instead of the global scope, as stack is a global variable
