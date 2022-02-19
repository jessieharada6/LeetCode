# 1675. Minimize Deviation in Array 19 Feb 2022

https://leetcode.com/problems/minimize-deviation-in-array/

- for loop
    ```
    for i in range(len(nums))
    for (int i = 0; i < nums.length; i++)
    ```
    i is a reference to the element of the list <br/>
    it can update the actual value in the list <br/>

    range() object is lazy loading - won't generate until requested <br/>
    more efficient than list() and tuple() where it forces all values returned at once <br/>

    ```
    for num in nums
    foreach(var num in nums)
    ```
    read only <br/>
    in python: iterable
    in C#: IEnumerable -> GetEnumerator() -> IEnumerator -> object Current, MoveNext(), Reset()
            ```
            IEnumerable 

            public IEnumerator GetEnumerator();

            IEnumerator

            public object Current;
            public void Reset();
            public bool MoveNext();
            
            // similar to
            public void foreach(Action<T>) {}
            ```
            [Link text Here] https://stackoverflow.com/questions/619564/what-is-the-difference-between-ienumerator-and-ienumerable 

- heap in python
    it is minHeap by default
    ```
    queue = []
    # form heap - usage: data structure
    heapq.heapify(queue)
    # remove the min element from heap - usage: get min
    heapq.heappop(queue)
    # update the heap with a new value - usage: insert a value and form heap
    heapq.heappush(queue,8)
    # remove the min element, and replace with another value - usage: 
    heapq.heapreplace(H,6)
    ```
    