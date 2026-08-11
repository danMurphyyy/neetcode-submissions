class Solution:
    def isValid(self, s: str) -> bool:
        # map opening brackets to their closing brackets
        bracketMap = {")": "(", "}": "{", "]": "["}
        stack = []

        for character in s:
            if character not in bracketMap: # is an opening bracket
                stack.append(character)
            else: # is a closing bracket
                #check if stackis empty or top doesn't match
                if not stack or stack[-1] != bracketMap[character]:
                    return False
                stack.pop()

        return not stack # True if the stack is empty