class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        group = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in group:
                if stack and stack[-1] == group[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False