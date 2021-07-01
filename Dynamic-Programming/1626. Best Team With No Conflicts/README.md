# 1626. Best Team With No Conflicts

https://leetcode.com/problems/best-team-with-no-conflicts/

"A conflict exists if a younger player has a strictly higher score than an older player."
This means that the oldest player's score should come first in the array, with the youngest's score being the last in the array.

1. Sort the ages descendingly (from the highest to the lowest).
2. Update the positions of the scores accordingly.
3. If the ages are the same, sort the scores descendingly. As we only include the scores that are greater than or equal to the current point of the score.

With the updated scores, as the age is from the most senior to the least senior, we can ignore ages.We need to ensure that all scores before the current score is greater or equal to the current score.
We must ensure that every score before the current score is greater than or equal to each other.

For example:
3 10 5 1

Suppose that i is at 1, dp[i] = 1, the updated dp array is [3, 10, 15, 1]
is 3 >= 1? yes:
so we update dp[i] to max(dp[i], 1 + 3), now dp[i] is 4
is 10 >= 1? yes:
but 3 is less than 1, we would like to select 10 in this case over 3
so we update dp[i] to max(dp[i], 1 + 10), now dp[i] is 11
is 5 >= 1? yes:
so we update dp[i] to max(dp[i], 1 + 15), now dp[i] is 16

So score is the criteria, in which it compares to the current score (where j is), and update scores in the dp array

```
if (currentScore >= score):
    dp[i] = max(dp[i], currentScore + score)
```

In the example below:

```
[1,3,7,3,2,4,10,7,5]
[4,5,2,1,1,2,4,1,4]
```

| sortedScores | 3   | 10  | 5   | 1   | 7   | 4   | 7   | 3   | 2   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dp           | 3   | 10  | 15  | 16  | 17  | 21  | 24  | 27  | 29  |
| sortedAges   | 5   | 4   | 4   | 4   | 2   | 2   | 1   | 1   | 1   |
