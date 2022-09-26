class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        
        time = [0]
        for t in travel:
            time.append(time[-1] + t)
        
        stops = defaultdict(int)
        for i, gar in enumerate(garbage):
            for g in gar:
                stops[g] = i
                res += 1
        
        # print(time, stops)
        
        for k, v in stops.items():
            res += time[v]
        
        return res


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        
        # time = [0]
        # for t in travel:
        #     time.append(time[-1] + t)
        time = list(accumulate(travel, initial=0))
        
        stops = defaultdict(int)
        for i, gar in enumerate(garbage):
            res += len(gar)
            for g in gar:
                stops[g] = i
                # res += 1
                
        for s in stops.values():
            res += time[s]
        
        return res

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        
        stops = defaultdict(int)
        for i, gar in enumerate(garbage):
            res += len(gar)
            for g in gar:
                stops[g] = i
                
        for s in stops.values():
            res += sum(travel[:s])
        
        return res
            