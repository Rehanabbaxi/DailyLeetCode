from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i in range(len(tickets)):
            if i <= k :
                res += min(tickets[i] , tickets[k])
            else:
               res += min(tickets[i] ,  tickets[k] - 1)

        return res 
    
solution = Solution()
test_tickets = [5,1,1,1]
K = 0

result = solution.timeRequiredToBuy(test_tickets , K)
print(result)