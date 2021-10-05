# 2027. Minimum Moves to Convert String

https://leetcode.com/contest/weekly-contest-261/problems/minimum-moves-to-convert-string/

one pass
for loop won't work, as if we jump every 3 elements, for example
sample = "This is a string"

for x in sample[::3]:
    print(x)

it only gets to literally every 3rd element, won't be one by one 

while is better, with one pass
if it's an X, then +1 for the output and jump 3 characters ahead
if not, then jump 1 character ahead to check the next