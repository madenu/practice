# # Rotate Array
# # https://leetcode.com/problems/rotate-array/
#
# # WORK IN PROGRESS
# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         len_nums = len(nums)
#         while k > 0:
#             next_k = k % len_nums
#             k = k // nums
#             end = nums[-k:]
#             nums[k:] = nums[:len_nums-k]
#             nums[:k] = end
#             k = next_k
#
#
# if __name__ == '__main__':
#     sol = Solution()
#     nums = [1, 2, 3, 4, 5, 6, 7]
#     k = 3
#     expected = [5, 6, 7, 1, 2, 3, 4]
#     sol.rotate(nums, k)
#     print(nums)
