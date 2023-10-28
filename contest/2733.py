#
# 9558 / 9558 test cases passed.
# Status: Accepted
# Runtime: 339 ms
# Memory Usage: 16.1 MB

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        max_num = max(nums)
        min_num = min(nums)
        for i in nums:
            if(i != max_num and i !=min_num):
                return i;
        return -1