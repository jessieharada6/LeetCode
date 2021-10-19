# 2018. Check if Word Can Be Placed In Crossword

https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

find the pattern, note that it must be next to #, starting from the edge of the cell 

zip(*word)
To print, print(list(*iterable))
* is to unpack the iterative argument 
rotate 90 degrees, right to left becomes top to bottom, and bottom to top becomes left to right

word[::-1]:
abc becomes cda

q = ''.join(cell).split("#")
make each row as a string 
split by #
so if #, the element is ''
if not, the element is as it is

# this question should be re-visited