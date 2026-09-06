class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for el in tokens:
            # print(stack, el)
            if el not in '/*+-':
                stack.append(int(el))
            else:
                b = stack.pop()
                a = stack.pop()
                ans = 0
                if el == '/':
                    ans = int(a/b)
                elif el == '+':
                    ans= a+b
                elif el == '*':
                    ans = a *b
                elif el == '-':
                    ans = a-b

                stack.append(ans)
        return stack.pop()