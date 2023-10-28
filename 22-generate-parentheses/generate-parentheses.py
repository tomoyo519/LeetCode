class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result =[]
        def rec(open, close, s):
            if open == n == close:
                result.append(s)
                return
            if open <=n :
                rec(open+1, close, s+'(')
            if close < open :
                rec(open, close +1, s+')')
        rec(1,0,'(')
        return result