from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(0 , len(nums)):
            if nums[i] != val:
                nums[j] =  nums[i]
                j += 1
        return j 
    
solution = Solution()
Test_List = [3,2,2,3]
Test_val = 3
Result_val = solution.removeElement(Test_List , Test_val)
print(Result_val)
print(Test_List)