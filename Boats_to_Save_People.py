from typing import List 
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        left , right = 0 , len(people)-1

        while left <= right :
            remaining = limit -  people[right]
            right -= 1 
            boat += 1

            if left <= right and remaining >= people[left] :
                left +=1
        return boat
    
solution = Solution()
Testing_List = [3,2,2,1]
Testing_limit = 3
result = solution.numRescueBoats(Testing_List , Testing_limit)
print(result)