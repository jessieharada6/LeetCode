class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        output = [0] * len(tasks)
        
        available = [(servers[i], i) for i in range(len(servers))]
        #min heap
        heapq.heapify(available)
        
        unavailable = []
        t = 0
        
        for i in range(len(tasks)):
            t = max(i, t)
            
            if len(available) == 0:
                t = unavailable[0][0]
            while unavailable and t >= unavailable[0][0]:
                time_free, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))
            
            #min heap pop the smallest item
            weight, index = heapq.heappop(available)
            output[i] = index
            heapq.heappush(unavailable, (t + tasks[i], weight, index))
        return output

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        output = [0] * len(tasks)
        
        #available: (server, index)
        #unavailable: (timeServerBecomesFree, server, index)
        
        available = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(available)
        #print(available)
        unavailable = []
        t = 0
        
        for i in range(len(tasks)):
            t = max(i, t)
            
            if len(available) == 0:
                t = unavailable[0][0]
            while unavailable and t >= unavailable[0][0]:
                time_free, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))
            
            weight, index = heapq.heappop(available)
            #print(weight, index)
            output[i] = index
            heapq.heappush(unavailable, (t + tasks[i], weight, index))
                
        return output
        
        
        
        