# https://leetcode.com/problems/merge-sorted-array
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        idx1, idx2, = 0, 0
        while (idx1 < m) and (idx2 < n):

            while (idx1 < m) and (idx2 < n) and (temp[idx1] <= nums2[idx2]):
                print(f"idx1: {idx1} temp1[idx1]: {temp[idx1]} idx2: {idx2} nums2[idx2] {nums2[idx2]}")
                nums1[idx1 + idx2] = temp[idx1]
                idx1 = idx1 + 1

            while (idx1 < m) and (idx2 < n) and (nums2[idx2] <= temp[idx1]):
                print(f"idx1: {idx1} temp1[idx1]: {temp[idx1]} idx2: {idx2} nums2[idx2] {nums2[idx2]}")
                nums1[idx1 + idx2] = nums2[idx2]
                idx2 = idx2 + 1

        while idx1 < m:
            nums1[idx1 + idx2] = temp[idx1]
            idx1 = idx1 + 1

        while idx2 < n:
            nums1[idx1 + idx2] = nums2[idx2]
            idx2 = idx2 + 1


if __name__ == '__main__':
    sol = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    sol.merge(nums1, m, nums2, n)
