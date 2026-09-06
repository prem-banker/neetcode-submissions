class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            if i == 1:
                ans.append('()')
            else:
                newans = set()
                for par in ans:
                    for j in range(len(par)):
                        par2 = par[:j] + '(' + par[j:]
                        print(par2)
                        for k in range(j+1, len(par2)):
                            par3 = par2[:k] + ')' + par2[k:]
                            if isValid(par3):
                                newans.add(par3)
                ans = list(newans)
        return ans



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