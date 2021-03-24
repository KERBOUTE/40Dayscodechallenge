class Solution:
    def longestPalindrome(self, s):
     longest = 0
     index = 0
     for i in range(len(s)):
         for j in range(i+2, len(s)):
             temp = s[i:j+1]
             if temp == temp[::-1] and len(temp) > longest:
                 longest = len(temp)
                 index = i
     result = s[index : index + longest] if longest != 0 else None
     return result

# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
