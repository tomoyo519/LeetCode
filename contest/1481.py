
# 43 / 43 test cases passed.
# Status: Accepted
# Runtime: 402 ms
# Memory Usage: 36.8 MB

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arrCounter = collections.Counter(arr)
        arrCounterSort = sorted(arrCounter.items(), key=lambda x:x[1])

        removeElements = k

        for idx, [element, count] in enumerate(arrCounterSort):
            if removeElements == 0 or removeElements < count:
                return len(arrCounter)
            
            if removeElements >= count:
                removeElements -= count
                del arrCounter[element]

        
        return len(arrCounter)