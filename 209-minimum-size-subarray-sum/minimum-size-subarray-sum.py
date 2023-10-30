class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums) < target: return 0
        total, left, answer = 0, 0, len(nums)
        for right, value in enumerate(nums):
            total = total + value
            while total >=target:
                total -= nums[left]
                answer = min(answer, right-left +1)
                left +=1
        return answer