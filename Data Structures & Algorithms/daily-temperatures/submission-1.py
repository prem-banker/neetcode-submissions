class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i, el in enumerate(temperatures):
            res.append(0)
            if i !=0:
                j = len(stack) -1
                while(temperatures[stack[-1]] < el):
                    popped = stack.pop()
                    res[popped] = i-popped
                    j-=1
                    if j < 0:
                        break
            stack.append(i)
        return res