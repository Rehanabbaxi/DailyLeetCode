from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+" , "/" , "*" , "-"}:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append( a +  b)
                elif token == "*":
                    stack.append( a *  b)
                elif token == "/" : 
                    stack.append( int(b /a) )
                elif token == "-":
                    stack.append( b -  a)
            else :
                stack.append(int (token))   

        return stack[0] 
    
solution = Solution()
testing_list = ["2","1","+","3","*"]
result = solution.evalRPN(testing_list)
print(result)