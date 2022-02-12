# 127. Word Ladder

https://leetcode.com/problems/word-ladder/

# HashMap:
- add words to the list based on the pattern

# BFS:
- use set to ensure there's no repetition
- use deque to collect all the nodes that are one character diff from the current nodes
- increment output if alll current nodes are compared to the endWord
- check if current node is the same as endWord 