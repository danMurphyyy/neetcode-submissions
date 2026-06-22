class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Key: a number in the array nums
        #Value: count that the number appears in the array nums
        count = defaultdict(int)
        # res is the candidate integer (the number that has the highest count atm)
        # maxCount is the current maximum count 
        res, maxCount = 0,0 

        # loop through all numbers in the array nums
        for num in nums:
            count[num] += 1
            if count[num] > maxCount:
                res = num
            maxCount = max(count[num], maxCount)

        return res