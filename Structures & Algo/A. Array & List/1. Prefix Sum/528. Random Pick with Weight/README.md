# 528. Random Pick with Weight

https://leetcode.com/problems/random-pick-with-weight/

- Bisect

```
import bisect # import module

a = [1, 3, 6]
x = 4
i = bisect.bisect_left(a, x) 
print(i)

>> 2
```
source: https://medium.com/analytics-vidhya/bisect-module-in-python-6b78f8c37beb

- Random
```
random.random() * self.prefix[-1] 
>> [0, 6) if w = [1, 2, 3]
```