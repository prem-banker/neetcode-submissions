class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i, el in enumerate(temperatures):
            res.append(0)
            while(stack and temperatures[stack[-1]] < el):
                popped = stack.pop()
                res[popped] = i-popped
                
            stack.append(i)
        return res