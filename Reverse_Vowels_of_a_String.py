from typing import List 
class Solution:
    def reverseVowels(self, s: str) -> str:
        List = list(s)
        left  = 0 
        right = len(List) - 1
        vowels  = set("aeiouAEIOU")


        while left < right :
            if List[left]  not in vowels:
                left +=1
            if List[right]  not in vowels:
                right -= 1 
            else :
                temp = List[left]
                List[left] = List[right]
                List[right] = temp
                left += 1 
                right -= 1 
                res = "".join(List)
        return res

solution  = Solution() 
testing_string = "leetcode"
result = solution.reverseVowels(testing_string)
print(result)