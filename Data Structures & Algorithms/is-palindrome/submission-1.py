class Solution:
    def isPalindrome(self, s: str) -> bool:
        clearS = ""

        for i in s.lower():
            if i not in " ?!,.'-;:":
                clearS += i

        return clearS == clearS[::-1]
