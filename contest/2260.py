from typing import List
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # 연속된 카드를 구할때까지 최소한 몇장을 뒤집어야 하냐
        # 뒤집어서 확인하는건 반드시 처음부터 하는것은 아니다.
        # 동일한 카드가 없을 경우는 -1 을 리턴한다.
        answer = float("inf")
        unique_cards = set(cards)
        if(len(unique_cards) == len(cards)):
            return -1
        dict = {}
        for i in range(len(cards)):
            if cards[i] in dict:
                answer = min(answer, (i - dict[cards[i]]) +1 )
            dict[cards[i]] = i
            print(dict)
        
        if answer == float("inf"):
            return -1
        else:
            return answer
        
sol = Solution()
cards = [3,4,2,3,4,7]
print(sol.minimumCardPickup(cards))