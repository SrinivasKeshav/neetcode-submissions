class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {"]": "[", "}": "{", ")": "("}
        for i in s:
            if i in lookup:
                if stack and lookup[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return stack == []