#  https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s.lower() if c.isalnum()])

        p1, p2 = 0, len(s) - 1
        while p2 >= 0:
            if s[p1] != s[p2]:
                return False

            p2 -= 1
            p1 += 1

        return True