class Solution:
    def isPalindrome(self, s: str) -> bool:
        noSpaceString = "".join(c.lower() for c in s if c.isalnum())
        pointerOne = 0
        pointerTwo = 0

        for character in range(len(noSpaceString)):
            pointerOne = character
            pointerTwo = len(noSpaceString) - 1 - character
            if noSpaceString[pointerOne] != noSpaceString[pointerTwo]:
                return False
            
        return True