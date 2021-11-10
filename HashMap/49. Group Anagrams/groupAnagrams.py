class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        output = []
        
        # sort each word ascendingly
        # add to dictionary as key with value as a list of index
        for i in range(len(strs)):
            c = ''.join(sorted(strs[i]))
            if not group.get(c):
                group[c] = [i]
            else:
                group[c].append(i)
    
        # print(group)
        
        # take the index and use the initial word from strs
        for key, value in group.items():
            current = []
            for v in value:
                # print(v, strs[v])
                current.append(strs[v])
            output.append(current)
        # print(output)
        
        return output