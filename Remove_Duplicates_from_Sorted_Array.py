from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0 
        n = len(nums)
        for i  in range(0 , n-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j += 1
        nums[j] = nums[n-1]
        return j+1
    
solution = Solution()
Test_List = [0,0,1,1,1,2,2,3,3,4]
print(Test_List)
result_val = solution.removeDuplicates(Test_List)
print(result_val)
print(Test_List)