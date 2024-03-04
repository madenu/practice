# 3Sum — Time limit exceeded
# https://leetcode.com/problems/3sum/

from collections import defaultdict


class Solution:
    def threeSum(self, nums: list[int]) -> list[tuple[int | list[int], ...]]:
        # Build pairs dict
        nums = sorted(nums)
        pairs = defaultdict(list[int])
        for ii in range(len(nums)):
            for jj in range(ii + 1, len(nums)):
                pairs[nums[ii] + nums[jj]].append((ii, jj))

        # Find answer
        result = set()
        for kk, num in enumerate(nums):
            for cand in pairs[-num]:
                if kk not in cand:
                    result.add(tuple(nums[idx] for idx in tuple(sorted(cand + (kk,)))))

        return result


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    actual = sol.threeSum(nums)
    print(actual)
