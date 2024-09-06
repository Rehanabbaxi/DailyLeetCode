from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle  = 0
        square = 0
        for choice in students:
            if choice == 0 :
                circle +=1
            else :
                square += 1
        
        for sandwich in sandwiches:
            if sandwich ==0 and circle == 0 :
                return square
            elif sandwich == 1 and square == 0:
                return circle
            elif sandwich == 0 :
                circle -= 1
            else :
                square -= 1
        return 0

solution = Solution()
test_students = [1,1,0,0]
test_sandwiches = [0,1,0,1]
result = solution.countStudents(test_students, test_sandwiches)
print(result)