# 127. Word Ladder

https://leetcode.com/problems/word-ladder/

- HashMap:
    add words to the list based on the pattern <br/>

- BFS:
    use set to ensure there's no repetition
    use deque to collect all the nodes that are one character diff from the current nodes <br/>
    increment output if alll current nodes are compared to the endWord <br/>
    check if current node is the same as endWord <br/>

- deque:
    use the code below to popleft() <br/>
    ```
    for _ in list(queue):
    ```
    if using normal for loop, it will pop the element as an object <br/>

    ```
    from collections import deque 

    q = deque([1, 2, 3])
    print(q)
    print(list(q))
    for _ in list(q):
        print(q.popleft())
    
    >> deque([1, 2, 3])
    >>[1, 2, 3]
    >> 1
    >> 2
    >> 3
    ```
