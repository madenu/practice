# 3Sum — Time limit exceeded
# https://leetcode.com/problems/3sum/

from collections import defaultdict


class Solution:
    def threeSum(self, nums: list[int]) -> list[tuple[int | list[int], ...]]:
        # Build pairs dict
        pairs = defaultdict(list[int])
        for ii in range(len(nums)):
            for jj in range(ii + 1, len(nums)):
                pairs[nums[ii] + nums[jj]].append((ii, jj))

        # Find answer
        result = []
        seen_idx = []
        seen_val = []
        for kk, num in enumerate(nums):
            for cand in pairs[-num]:
                if kk not in cand:
                    # Just get it done and move on.
                    # Look up the optimal solution afterward.
                    temp_idx = tuple(sorted(cand + (kk,)))
                    temp_val = tuple(sorted(nums[idx] for idx in temp_idx))
                    if temp_idx not in seen_idx and temp_val not in seen_val:
                        seen_idx.append(temp_idx)
                        seen_val.append(temp_val)
                        result.append(temp_val)

        return result


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    actual = sol.threeSum(nums)
    print(actual)
