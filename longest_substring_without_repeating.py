class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        lhs = 0
        rhs = 0
        while lhs < len(s) and rhs < len(s):
            if s[rhs] in seen:
                seen.remove(s[lhs])
                lhs += 1
            else:
                seen.add(s[rhs])
                res = max(res, rhs - lhs + 1)
                rhs += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "pwwkew"
    expected = 3
    actual = sol.lengthOfLongestSubstring(s)
    assert actual == expected
