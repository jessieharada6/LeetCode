# 1288. Remove Covered Intervals

https://leetcode.com/problems/remove-covered-intervals/

- Sorting
    ```
    # sort 1d
    array = [4,5,2,3]
    sorted(array)
    array.sort()
    ```

    ```
    # sort 2d
    intervals = [[1,4],[3,6],[2,8]]

    # increasing order - sort first element
    intervals.sort(key = lambda x : x[0])
    sorted(intervals, key = lambda x : x[0])

    # decreasing order
    intervals.sort(key = lambda x : -x[0])
    sorted(intervals, key = lambda x : -x[0])

    # increasing order first element
    # if first element is the same, decreasing order for the second element 
    intervals.sort(key = lambda x : (x[0], -x[1]))
    ```

- Traverse 2d array with 2 elements in each 
    ```
    for l, r in intervals:
        print(l, r)
    ```