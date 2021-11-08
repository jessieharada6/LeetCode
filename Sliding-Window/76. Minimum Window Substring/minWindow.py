class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        t_dict, window_dict = {}, {}
        l = 0
        res, res_len = [-1, -1], inf
        
        # init dictionary
        for c in t:
            t_dict[c] = 1 + t_dict.get(c, 0)
        
        have, need = 0, len(t_dict)
        
        # use for, so that r will not be added 1
        for r in range(len(s)):
            c = s[r]
            window_dict[c] = 1 + window_dict.get(c, 0)
            
            # update have
            if c in t_dict and window_dict[c] == t_dict[c]:
                have += 1
            
            while have == need:
                # print(l, r, res)
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)
                # left move forward
                window_dict[s[l]] -= 1
                # update have due to left moving forward
                if s[l] in t_dict and window_dict[s[l]] < t_dict[s[l]]:
                    have -= 1
                l += 1
        
        # print(l, r, res)
        # now l is actually + 1, but res is not
        l, r = res
        # print(l, r, res)
        
        return s[l:r + 1]          