class Solution:
    def reverse(self, x: int) -> int:

        array_x = list(str(x))
        array_x.reverse()
        solution = [];
        # [  '3','2','1', '-',]
        for i in range(len(array_x)):
            
            if( i == 0 and array_x[i] == 0 ):
                continue;
            if(array_x[i] == '-'):
                continue
            else:
                solution.append(array_x[i])    
        result = int(''.join(solution))

        if result > (2 ** 31) - 1 or result < -(2 ** 31):
            return 0
        if (x <0):
            return result * (-1)
        else:
            return result

