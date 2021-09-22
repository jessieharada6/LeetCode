# 399. Evaluate Division

https://leetcode.com/problems/evaluate-division/


Useful links: 
https://leetcode.com/problems/evaluate-division/discuss/270993/Python-BFS-and-UF(detailed-explanation)
https://leetcode.com/problems/evaluate-division/discuss/700017/Python-Very-Clean-and-simple-DFS-Solution
https://leetcode.com/problems/evaluate-division/discuss/638479/Javascript-DFS-Solution

Union Find:
https://www.youtube.com/watch?v=ibjEGG7ylHk 
https://www.youtube.com/watch?v=0jNmHPfA_yE
https://www.youtube.com/watch?v=VHRhJWacxis

Sourced from:https://stackoverflow.com/questions/53871059/how-to-zip-three-lists-into-a-nested-dict/53871116

The function zip() can accept more than two iterables. So you can use zip(z1, z2, z3) instead of zip(z2, z3). However, you still need to group the items since simply wrapping dict() will not work as it can't handle nested dictionaries needed for the 3-tuples.

To group the items correctly, I would use a collections.defaultdict():

```
from collections import defaultdict

z1 = ['A', 'A', 'B', 'B']
z2 = ['k1', 'k2', 'k1', 'k2']
z3 = ['v1', 'v2', 'v3', 'v4']

d = defaultdict(dict)
for x, y, z in zip(z1, z2, z3):
    d[x][y] = z

print(d)
# defaultdict(<class 'dict'>, {'A': {'k1': 'v1', 'k2': 'v2'}, 'B': {'k1': 'v3', 'k2': 'v4'}})
```

The above works because defaultdict(dict) initializes a dictionary for non-existent keys. It handles the dictionary creation for keys for you.

Additionally, If you wrap the end result with dict:
```
print(dict(d))
# {'A': {'k1': 'v1', 'k2': 'v2'}, 'B': {'k1': 'v3', 'k2': 'v4'}}
```

Note: defaultdict is just a subclass of dict, so you can treat it the same as a normal dictionary.

