# 207. Course Schedule

https://leetcode.com/problems/course-schedule/

Useful link: 
https://www.youtube.com/watch?v=EgI5nU9etnU
https://leetcode.com/problems/course-schedule/discuss/1403888/Javascript-DFS-with-Clear-Explanation

!!! Both for..of and for..in statements iterate over lists; 
the values iterated on are different though, for..in returns a list of keys on the object being iterated, whereas for..of returns a list of values of the numeric properties of the object being iterated.

* build a map based on each course => [pre]
* use a set to check which course has been visited, if there's a repetition, return false