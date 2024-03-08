# https://leetcode.com/problems/count-elements-with-maximum-frequency/

from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:

        freqs = Counter(nums)
        max_freq = max(freqs.values())

        count = 0
        for freq in freqs.values():
            if freq == max_freq:
                count += max_freq

        return count
