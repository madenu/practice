# Rotate Array
# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        rotations = 0
        end = None
        while rotations < k:
            end = nums[-1]
            for i in range(len_nums - 1, -1, -1):
                nums[i] = nums[i - 1]
            nums[0] = end
            rotations += 1


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    expected = [5, 6, 7, 1, 2, 3, 4]
    sol.rotate(nums, k)
    print(nums)
