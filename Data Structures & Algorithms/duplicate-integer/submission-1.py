class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}

        for n in nums:
            if n in dictionary:
                return True
            else:
                dictionary[n] = n

        return False