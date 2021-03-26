class Solution:
  def getRange(self, arr, target):
    index=arr.index(target)
    return [index, index+arr.count(target)-1] if target in arr else [-1,-1]

# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
