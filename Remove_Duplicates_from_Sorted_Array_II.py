from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1 
        index = 1
        for i in range(1 , len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else :
                count = 1
            if count <= 2 :
                nums[index] = nums[i]
                index +=1
        return index
    
solution = Solution()
Testing_List = [1,1,1,2,2,3]
print(Testing_List)
result_val = solution.removeDuplicates(Testing_List)
print(result_val)
print(Testing_List)