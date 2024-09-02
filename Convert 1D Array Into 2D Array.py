from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        else:
            stack = original[::-1]
            result = []
            for i in range(m):
                row = []
                for j in range(n):
                    row.append(stack.pop())
                result.append(row)
        return result

solution = Solution()
test_list = original = [1,2,3,4]
m  =  2
n= 2
res = solution.construct2DArray(test_list , m , n)
print(res)