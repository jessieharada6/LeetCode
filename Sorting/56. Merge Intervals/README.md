# 56. Merge Intervals

https://leetcode.com/problems/merge-intervals/

- merge on current right point and the next left point
    when current right point <= next left point: <br/>
        compare these two points <br/>
        use the first element as base <br/>
        update the right point max() <br/>
    when current right point > next left point:  <br/>
        add in a new element  <br/>