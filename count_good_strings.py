# https://leetcode.com/problems/count-ways-to-build-good-strings/
from collections import defaultdict


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = defaultdict(int)
        Solution._count_good(low, high, zero, one, 0 + zero - 1, dp, set(), 0b0)
        Solution._count_good(low, high, zero, one, 0 + one - 1, dp, set(), 0b1)
        return sum(dp.values()) % (10 ** 9 + 7)

    @staticmethod
    def _count_good(low, high, zero, one, jj, dp, seen, append_id):
        # Note: Multiplication is commutative

        if (jj, append_id) in seen:  # We've already been here
            return

        if jj >= high:  # Max length exceeded
            return

        if jj + 1 - low > -1:  # Minimum length reached
            # Because len(jj) is only ever increased by "zero" or "one", I know this is a good string
            dp[jj] = (dp[jj] + 1) % (10 ** 9 + 7)

        seen.add((jj, append_id))
        Solution._count_good(low, high, zero, one, jj + zero, dp, seen, (append_id << 1 | 0b0))
        Solution._count_good(low, high, zero, one, jj + one, dp, seen, (append_id << 1 | 0b1))


if __name__ == '__main__':
    sol = Solution()

    # low, high, zero, one = 3, 3, 1, 1
    # expected = 8
    # actual = sol.countGoodStrings(low, high, zero, one)
    # print(actual)
    # assert actual == expected

    # TODO This keeps going
    #      I think I need to use "zero" and "one" to find another base case or to set bounds
    low, high, zero, one = 200, 200, 10, 1
    expected = 2  # All zeros or all ones
    actual = sol.countGoodStrings(low, high, zero, one)
    print(actual)
    assert actual == expected
