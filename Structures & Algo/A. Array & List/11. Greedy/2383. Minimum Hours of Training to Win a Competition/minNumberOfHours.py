class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        res = 0
        for x, y in zip(energy, experience):
            if initialEnergy <= x:
                res += x + 1 - initialEnergy
                initialEnergy = x + 1
            initialEnergy -= x
            
            if initialExperience <= y:
                res += y + 1 - initialExperience
                initialExperience = y + 1
            initialExperience += y
        
        return res