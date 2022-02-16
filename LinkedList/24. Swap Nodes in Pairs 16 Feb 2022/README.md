# 24. Swap Nodes in Pairs

https://leetcode.com/problems/swap-nodes-in-pairs/

1. pay attention to the updated position pointers </br>

    To avoid cycle detection error </br>
    second.next must be updated only after first.next is updated </br>
    if we point second.next to first, then update first.next to second.next, two nodes will be pointing towards each other </br>

```
# update pointers
current.next = second
first.next = second.next
second.next = first
```

2. need to check current.next for the last node </br>
    at the last node, the node object still has .next attribute </br>
    if only checking current.next.next </br>
    for the last node, there's no object remaining nor the .next attribute </br>

```
while current.next and current.next.next:
```