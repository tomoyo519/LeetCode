class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 121
# // start, end 로 부터 뒤에서부터 만나서 다르면 false, 반복문 끝까지 돌았으면 true
        if(x < 0):
            return False
        
        start = 0

        array_x = list(str(x))
        # 2
        end = len(array_x) -1
        while(start != end and start >= 0 and end >= 0):
            if(array_x[start] != array_x[end]):
                return False
            elif(array_x[start] == array_x[end]):
                start +=1
                end -=1
            else:
                return False
            
        return True