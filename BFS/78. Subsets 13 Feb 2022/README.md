# 78. Subsets

https://leetcode.com/problems/subsets/

## IMPORTANT:
Using list.append modifies the list in place, including the original list! <br />
Using + CREATES a new list - joins/flatten the list - assignments involve rebinding

```
output = [1]
subset = output + [2]
print(subset, output) 
>> [1] [1, 2]
```

```
outputA = [1]
subsetA = outputA
subsetA.append(2)
print(subsetA, outputA) 
>> [1, 2] [1, 2]
```

<em>+ is a binary operator that produces a new list resulting from a concatenation of two operand lists.</em> <br/>
<em>append is an instance method that appends a single element to an existing list.</em> <br/>
sourced from: <br/>
https://stackoverflow.com/questions/11177533/whats-the-difference-between-plus-and-append-in-python-for-list-manipulation <br/>
https://stackoverflow.com/questions/725782/in-python-what-is-the-difference-between-append-and 

```
a = []
a.append([1, 2])
a.append([3, 4])
print(a)
>> [[1, 2], [3, 4]]
```

```
b = []
b += [1, 2]
b += [3, 4]
print(b)
>> [1, 2, 3, 4]
```

```
c = []
c += [[1, 2]]
c += [[3, 4]]
print(c)
>> [[1, 2], [3, 4]]
```