from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # recirsove 동서남북 1을 찾기, 하나라도있으면 count ++ 하지않고, 1의 위치에서 다시 동서남북 찾기.
        # left, right, top, bottom 그리고 끝에 다다랐는지,

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    self.helper(grid,i,j)
                    count +=1
        return count
    
    def helper(self, grid , i , j):
        queue = deque([(i,j)])
        while queue:
            I,J = queue.popleft()
            for i, j in [I+1, J], [I, J+1], [I-1, J], [I, J-1]:
                if 0<= i < len(grid) and 0<= j < len(grid[0]) and grid[i][j] =='1':
                    grid[i][j] = '0'
                    queue.append((i,j))
