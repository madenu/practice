# 3Sum — Time limit exceeded
# https://leetcode.com/problems/3sum/


class Solution:
    def threeSum(self, nums: list[int]):
        nums = sorted(nums)
        res = set()

        for ii in range(len(nums)):
            jj, kk = ii + 1, len(nums) - 1
            while jj < kk:
                amt = nums[ii] + nums[jj] + nums[kk]
                if amt == 0:
                    res.add((nums[ii], nums[jj], nums[kk]))
                    jj += 1
                    kk -= 1
                elif amt < 0:
                    jj += 1
                elif amt > 0:
                    kk -= 1

        return list(res)


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    actual = sol.threeSum(nums)
    print(actual)
