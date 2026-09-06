class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(opened, closed):
            if opened == n and closed == n:
                res.append(''.join(stack))
                return
            
            if opened < n:
                stack.append('(')
                backtrack(opened+1, closed)
                stack.pop()
            
            if opened > closed:
                stack.append(')')
                backtrack(opened, closed+1)
                stack.pop()
            
        backtrack(0,0)
        return res




def isValid(par):
    stack = []
    for el in par:  
        if el == '(':
            stack.append(el)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0