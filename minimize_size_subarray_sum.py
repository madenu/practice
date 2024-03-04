# https://leetcode.com/problems/minimum-size-subarray-sum/description/
# Contiguous subarray
# Sliding window
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        ans = float('inf')
        left, sum = 0, 0
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1

        return ans if ans < float('inf') else 0


if __name__ == '__main__':
    sol = Solution()

    nums = [1, 2, 3, 4, 5]
    target = 15
    expected = 5
    actual = sol.minSubArrayLen(target, nums)
    assert actual == expected

    nums = [1, 2, 3, 4, 5]
    target = 11
    expected = 3
    actual = sol.minSubArrayLen(target, nums)
    assert actual == expected

    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    target = 11
    expected = 0
    actual = sol.minSubArrayLen(target, nums)
    assert actual == expected
