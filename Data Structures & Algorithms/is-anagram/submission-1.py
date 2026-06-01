class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        stringOneDictionary = {}

        for character in s:
            stringOneDictionary[character] = stringOneDictionary.get(character, 0) + 1

        for character in t:
            if character not in stringOneDictionary:
                return False
            stringOneDictionary[character] -= 1
            if stringOneDictionary[character] == 0:
                del stringOneDictionary[character]

        return len(stringOneDictionary) == 0
    