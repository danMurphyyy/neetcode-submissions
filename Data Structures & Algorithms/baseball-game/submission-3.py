class Solution:
    def calPoints(self, operations: List[str]) -> int:
        returnStack = []

        for num in operations:
            if num == "+":
                result = returnStack[-1] + returnStack[-2]
                returnStack.append(result)
            elif num == "D":
                result = returnStack[-1] * 2
                returnStack.append(result)
            elif num == "C":
                returnStack.pop()
            else:
                returnStack.append(int(num))
                
        return sum(returnStack)