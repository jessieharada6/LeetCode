# 370. Range Addition

Assume you have an array of length n initialized with all 0's and are given k update operations. <br/>
Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.<br/>
Return the modified array after all k operations were executed.<br/>


Example:<br/>
Given:<br/>

    length = 5,
    updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
    ]

Output:<br/>
[-2, 0, 3, 5, 3]

Explanation: <br/>
Initial state: <br/>
[ 0, 0, 0, 0, 0 ]

After applying operation [1, 3, 2]: <br/>
[ 0, 2, 2, 2, 0 ]

After applying operation [2, 4, 3]: <br/>
[ 0, 2, 5, 5, 3 ]

After applying operation [0, 2, -2]: <br/>
[-2, 0, 3, 5, 3 ]
