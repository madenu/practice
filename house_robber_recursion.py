# https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: list[int]) -> int:
        return Solution._rob(nums, 0, {})

    @staticmethod
    def _rob(nums, idx, dp):
        if idx >= len(nums):  # Index out of bounds
            dp[idx] = 0
            return 0
        if idx == len(nums) - 1:  # Last index
            dp[idx] = nums[idx]
            return dp[idx]
        if idx not in dp:
            dp[idx] = max(Solution._rob(nums, idx + 1, dp),
                          Solution._rob(nums, idx + 2, dp) + nums[idx])
        return dp[idx]
