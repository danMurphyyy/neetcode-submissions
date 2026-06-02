class Solution:

    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for characters in string:
                count[ord(characters) - ord("a")] += 1
            groups[tuple(count)].append(string)
        return list(groups.values())