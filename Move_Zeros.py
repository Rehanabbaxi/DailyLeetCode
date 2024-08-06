from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0  
        n = len(nums)
        
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        for i in range(j, n):
            nums[i] = 0
        return nums 

solution = Solution()
TestList = [0,1,0,3,12]
result = solution.moveZeroes(TestList)
print(result)