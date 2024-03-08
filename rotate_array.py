# Rotate Array
# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        k = k % len_nums
        if k == 0 or len_nums < 2:
            return
        end = nums[-k:]
        nums[k:] = nums[:len_nums - k]
        nums[:k] = end


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    expected = [5, 6, 7, 1, 2, 3, 4]
    sol.rotate(nums, k)
    print(nums)
