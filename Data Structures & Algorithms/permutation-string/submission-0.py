class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        for i in s1:
            counts1[i] = 1 + counts1.get(i, 0)
        
        for l in range(len(s2) - len(s1) + 1):
            counts2 = {}
            for r in range(l, l + len(s1)):
                counts2[s2[r]] = 1 + counts2.get(s2[r], 0)
            if counts1 == counts2:
                return True

        return False
