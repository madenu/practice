# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution:
    def minimumLength(self, s: str) -> int:
        len_s = len(s)
        pre, suf = 0, len_s - 1
        while suf - pre > 0 and s[pre] == s[suf]:
            _pre = pre
            while pre < len_s and s[pre] == s[_pre]:
                pre += 1
            _suf = suf
            while suf > pre and s[suf] == s[_suf]:
                suf -= 1
        return suf - pre + 1


if __name__ == '__main__':
    sol = Solution()

    s = "cabaabac"
    expected = 0
    assert expected == sol.minimumLength(s)

    s = "ca"
    expected = 2
    assert expected == sol.minimumLength(s)

    s = "aabccabba"
    expected = 3
    assert expected == sol.minimumLength(s)

    s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
    expected = 1
    assert expected == sol.minimumLength(s)
