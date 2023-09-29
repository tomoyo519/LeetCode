class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = 0;
#          [4,4,2,4,3]
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if(nums[i] != nums[j] != nums[k] and i<j<k):
                        count+=1;
        return count
        
        