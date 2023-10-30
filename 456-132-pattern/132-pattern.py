class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        # // 브루트 포스 말고 있나 ...?
        stack = []
        max3 = float('-inf')
    #    start = 맨 뒤에서부터, stop = -1로 0번 이전 위치, step 은 -1로 인덱스를 1씩 감소시킴
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < max3:
                return True
            while stack and stack[-1] < nums[i]:
                max3 = stack[-1]
                stack.pop()
            stack.append(nums[i])
        return False