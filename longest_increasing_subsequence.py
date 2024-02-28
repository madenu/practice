def longest(nums):
    seen = {k: 1 for k in range(len(nums))}  # Initialize to shortest possible subsequence length

    for ii in range(len(nums)):  # Work from the bottom up
        max_len = 1
        for jj in range(ii, -1, -1):  # Check previous indices
            if (nums[ii] > nums[jj]) and (seen[jj] + 1 > max_len):
                max_len = seen[jj] + 1
        seen[ii] = max_len

    return max(seen.values())


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 2, 3]  # 4
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]  # 4
    # nums = [4, 10, 4, 3, 8, 9]  # 3
    print(longest(nums))
