class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_dict = {')' : '(', ']' : '[', '}' : '{'}
        
        for c in s:
            if c in parentheses_dict:
                if stack and stack[-1] == parentheses_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False


        