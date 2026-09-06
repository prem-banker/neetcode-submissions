class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        n = len(s)
        stack = []
        for el in s:
            if el in '({[':
                stack.append(el)
            elif el in ')}]':
                if len(stack) <=0:
                    return False
                else:
                    popped = stack.pop()
                    if el == ')' and popped != '(':
                        return False
                    if el == ']' and popped != '[':
                        return False
                    if el == '}' and popped != '{':
                        return False

        return stack == []