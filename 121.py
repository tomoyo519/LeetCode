from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 앞에서부터 min값을 찾기, 그 idx 이후의 max값을 찾아서 팔기 idx 비교하기
        min_num = min(prices)
        print('min_num',min_num)
        min_idx = 0
        for  idx, num in enumerate(prices):
            print('num', num)
            if num == min_num:
                min_idx = idx
        max_num = 0
        print('min_idx', min_idx)
        for i in range(min_idx, len(prices)):
            print('i',i)
            if(max_num < prices[i]):
                max_num = prices[i]
        print('max_num',max_num)
        print('min_num',min_num)
        if(max_num - min_num <= 0):
            return 0
        else:
            return (max_num - min_num)
sol = Solution()
prices = [2,4,1]
print(sol.maxProfit(prices))

