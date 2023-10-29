class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        presum = 0
        d = {0:1}
        for num in nums:
            presum = presum + num
            if(presum - k) in d:
                result = result + d[presum - k]
            if presum not in d:
                d[presum] = 1
            else:
                d[presum] = d[presum] + 1
        print(d)
        return result