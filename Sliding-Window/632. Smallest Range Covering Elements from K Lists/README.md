# 632. Smallest Range Covering Elements from K Lists

https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

- enumerate()
    ```
    # first param is always index, second param is the element
    for index, num in enumerate(nums):
        print(index, num)
    ```
    ```
    # by default, start (i.e. index counts) is 0, but can redefine the start
    # so that the index starts from 1
    for index, num in enumerate(nums, start = 1):
        print(index, num)
    ```