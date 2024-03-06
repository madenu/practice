class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        ii = 1
        jj = 1
        count = 0
        prev = nums[0]
        while jj < len(nums):
            if nums[jj] == prev:
                count += 1

            if count == 2:
                while jj < len(nums) and nums[jj] == prev:
                    jj += 1
                count = 0

            nums[ii] = nums[jj]
            ii += 1
            jj += 1

        print(nums)
        return ii


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    sol.removeDuplicates(nums)
