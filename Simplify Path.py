class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in path.split("/"):
            if i == ".." :
                if stack :
                    stack.pop()
            elif i == "." or i == "" :
                continue
            else :
                stack.append(i)
        
        res = "/" + "/".join(stack)
        return res

solution = Solution()
testing_path = "/home/user//Documents/../Pictures"
result = solution.simplifyPath(testing_path)
print(result)