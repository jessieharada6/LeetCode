class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key = lambda x : (x[0], -x[1]))
    
        n = len(clips)
        res, i, cur_end, next_end = 0, 0, 0, 0
        
        while i < n and clips[i][0] <= cur_end:
            while i < n and clips[i][0] <= cur_end:
                next_end = max(next_end, clips[i][1])
                i += 1
            res += 1
            cur_end = next_end
            if cur_end >= time:
                return res
        
        return -1