class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNumOfOnes = 0
        temp = 0

        for num in nums:
            if num == 1:
                temp += 1
            else:
                maxNumOfOnes = max(maxNumOfOnes, temp)
                temp = 0

        return max(maxNumOfOnes, temp)