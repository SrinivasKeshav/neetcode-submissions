class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        x, y = {}, {}
        for i, j in zip(s, t):
            x[i] = x.get(i, 0) + 1
            y[j] = y.get(j, 0) + 1
        return x==y