class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        rightArr = [1] * len(nums)
        leftArr = [1] * len(nums)

        for i in range(1, len(nums)):
            leftArr[i] = leftArr[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            rightArr[i] = rightArr[i+1] * nums[i+1]

        for i in range(len(nums)):
            output[i] = leftArr[i] * rightArr[i]

        return output