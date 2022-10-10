class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ands = set()
        ans = set()
        
        for x in arr:
            ands = { x & a for a in ands }
            ands.add(x)
            ans |= ands
        
        # diff = inf
        # for a in ans:
        #     diff = min(diff, abs(target - a))
        
        return min(abs(target - a) for a in ans)
            