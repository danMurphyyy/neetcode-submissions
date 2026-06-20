class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        currentCount = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                currentCount = currentCount + 1

                if currentCount > count:
                    count = currentCount

            elif nums[i] == 0:
                currentCount = 0

        return count