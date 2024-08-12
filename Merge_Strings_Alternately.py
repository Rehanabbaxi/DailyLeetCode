from typing import List 

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0
        for i in range(max(len(word1) , len(word2))):
            if i < len(word1):
                result += word1[i]
            if i < len(word2) : 
                result += word2[i]
        return result
    
solution = Solution()
Test_word1 = "ace"
Test_word2  = "bdfhj"
result = solution.mergeAlternately(Test_word1 , Test_word2)
print(result)