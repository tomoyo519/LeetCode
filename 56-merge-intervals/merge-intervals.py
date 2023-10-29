class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        # 0,1,2
        intervals = sorted(intervals, key=lambda x: x [0])
        for i in intervals:
            if not result or result[-1][1] < i[0]:
                result.append(i)
            else:
                result[-1][1] = max(result[-1][1], i[1])

        return result