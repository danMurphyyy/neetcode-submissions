class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesesDict = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in parenthesesDict:
                if stack and stack[-1] == parenthesesDict[c]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)

        if not stack:
            return True
        else: 
            return False