class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNumOfOnes = 0
        temp = 0

        for x in range(len(nums)):
            if nums[x] == 1:
                temp += 1
            else:
                maxNumOfOnes = max(maxNumOfOnes, temp)
                temp = 0

        return max(maxNumOfOnes, temp)