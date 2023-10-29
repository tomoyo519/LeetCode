class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # 각 문자가 나타난 위치
        used = {}
        # start = 현재 부분 문자열
        # max_length = 지금까지 발견한 가장 긴 부분 문자열의 길이

        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] +1
            else:
                max_length = max(max_length, i - start +1)

            used[c] = i
        return max_length