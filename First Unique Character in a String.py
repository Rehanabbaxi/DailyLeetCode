from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)

        for c in s:
            count[c] += 1
        
        for i , c in enumerate(s):
            if count[c] == 1:
                return i
        return -1

solution = Solution()
test_str = "leetcode"
result = solution.firstUniqChar(test_str)
print(result)