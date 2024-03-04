class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        ans = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[right] >= height[left]:
                left += 1
            else:
                right -= 1
            ans = max(ans, min(height[left], height[right]) * (right - left))
        return ans


if __name__ == '__main__':
    sol = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    expected = 49
    actual = sol.maxArea(height)
    assert actual == expected

    sol = Solution()
    height = [1, 2, 4, 3]
    expected = 4
    actual = sol.maxArea(height)
    assert actual == expected
