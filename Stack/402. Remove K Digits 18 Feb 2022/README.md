# 402. Remove K Digits

https://leetcode.com/problems/remove-k-digits/

- stack
```
stack.pop()
# remove element from the right side
stack.append()
# append element from the right side
```

- while 
while loop will always check one more time until the condition is not met <br/>
```
while stack and k and int(stack[-1]) > int(n):
    stack.pop()
    k -= 1
stack.append(n)
```
For example: num = "1432219" k = 3 <br/>
At one stage, stack is ["1", "2"] <br/>
1. stack will then be ["1", "2", "2"], "2" will be popped as the current int(n) is 1 <br/>
    stack will be ["1", "2"] <br/>
2. then "2" will be removed again, because while loop will go back to check whether the condition is met <br/>
    stack will be ["1"] <br/>
3. code then proceeds to stack.append(n)
    stack will be ["1", "1"] <br/>