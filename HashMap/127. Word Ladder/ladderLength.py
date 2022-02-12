class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        output = 0
        
        # edge case
        if endWord not in wordList:
            return output
        
        # 1. HASHMAP
        # key -> pattern e.g. hit -> *it, h*t, hi*
        # value -> list that conforms to the pattern
        hashMap = collections.defaultdict(list)
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                hashMap[pattern].append(word)
        
        # print(hashMap)
        
        # 2. BFS
        visit = set([beginWord])
        queue = collections.deque([beginWord])
        
        # as beginWord is the first node which is already in the queue
        output = 1
        while queue:
            # queue contains all the neighbour words for the previous word
            for _ in list(queue):
                word = queue.popleft()
                # print("current node: ", word)
                if word == endWord:
                    return output
                
                # add all the unvisted neighbour words to the queue
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    # print("pattern", pattern)
                    for neiWord in hashMap[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            queue.append(neiWord)
                            # print("next nodes:   ", neiWord)
            
            # each finding presents the nodes that differ from the previous words by 1 character
            # increment only if all the current nodes are compared with endWord
            output += 1
        
        # no nodes can lead to endWord
        return 0