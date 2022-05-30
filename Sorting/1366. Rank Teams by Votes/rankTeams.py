class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # ["ABC","ACB","ABC","ACB","ACB"]
        # record every team's vote in every position
        counts = {}
        ranking = ""
        
        # build dictionary
        # {'A': [5, 0, 0], 'B': [0, 2, 3], 'C': [0, 3, 2]}
        for vote in votes:
            for c in range(len(vote)):
                if vote[c] not in counts:
                    counts[vote[c]] = [0] * len(vote)
                counts[vote[c]][c] += 1
        print(counts)
        
        # sort dictionary by key alphabetically
        sorted_counts = sorted(counts.keys())
        # ['A', 'B', 'C']
        print(sorted_counts) 
        
        # key=lambda x: counts[x]  - go by columns - A, B, C for column 1 is 5, 0, 0; A, B, C for column 2 is 0, 2, 3
        # sort based on the ranking of each letter starting from index 0
        # normal sorting is ascending, but we need it for descending (larger number in the index represents higher ranking)
        return "".join(sorted(sorted_counts, key=lambda char: counts[char], reverse=True))
       