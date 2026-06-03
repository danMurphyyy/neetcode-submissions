class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyDict = {}
        results = []

        for num in nums:
            frequencyDict[num] = frequencyDict.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in frequencyDict.items():
            buckets[freq].append(num)

        for bucket in reversed(buckets):
            for num in bucket:
                results.append(num)
                if len(results) == k:
                    return results

        return results