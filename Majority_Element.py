from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]

solution = Solution()
Testing_list = [2,2,1,1,1,2,2]
result_val = solution.majorityElement(Testing_list)
print(result_val)