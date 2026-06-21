class Solution:

    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])

            if s[i] == ")":
                try:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                except:
                    return False

            if s[i] == "}":
                try:
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                except:
                    return False

            if s[i] == "]":
                try:
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                except:
                    return False

        if stack == []:
            return True

        else: return False