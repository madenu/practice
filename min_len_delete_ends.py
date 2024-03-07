# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution:
    def minimumLength(self, s: str) -> int:
        pre = 0
        suf = len(s) - 1
        res = s
        while len(res) > 1 and res[0] == res[-1]:

            prefix = ""
            while pre < len(s):
                if s[pre] == res[0]:
                    prefix += s[pre]
                    pre += 1
                else:
                    break

            suffix = ""
            while suf > pre:
                if s[suf] == res[0]:
                    suffix += s[suf]
                    suf -= 1
                else:
                    break

            res = s[pre:suf + 1]

        print(res)
        return len(res)


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
