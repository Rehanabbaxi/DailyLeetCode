
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair  =  [(p ,s) for p , s  in zip(position , speed)]
        pair.sort(reverse = True)

        stack = []
        for p,s in pair :
            stack.append((target - p)/ s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
         
solution_obj = Solution()
test_target = 12
test_position = [10,8,0,5,3]
test_speed = [2,4,1,1,3]

result = solution_obj.carFleet(test_target, test_position , test_speed)
print(result)