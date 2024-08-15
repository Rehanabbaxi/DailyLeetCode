from typing import List 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums)
        k = k % n
    
        def reverse(left , right):
            while left<= right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1 
                right -= 1 

        Left , Right =  0 , (n-k) - 1 
        reverse(Left , Right)

        Left , Right = n-k , n-1 
        reverse(Left , Right)

        Left , Right = 0 , n-1
        reverse(Left , Right)

        return nums 
    
solution = Solution()
Testing_list  = [-1,-100,3,99]
Testing_K = 2
result = solution.rotate(Testing_list , Testing_K)
print(result)