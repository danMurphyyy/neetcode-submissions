class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        suffix = []
        running = 1
        output = []

        for num in range(len(nums)):
            prefix.append(running)
            running = running * nums[num]

        running = 1

        for num in range(len(nums) - 1, -1, -1):
            suffix.append(running)
            running = running * nums[num]

        for i in range(len(nums)):
            output.append(prefix[i] * suffix[len(suffix) - 1 - i])

        return output