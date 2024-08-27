class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and c == "*":
                stack.pop()
            else:
                stack.append(c)
        res = ""
        res +=  res.join(stack)
        return res 
        
soluttion = Solution()
testing_str = "leet**cod*e"
result = soluttion.removeStars(testing_str)
print(result)