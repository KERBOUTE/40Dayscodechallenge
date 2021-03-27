def sortNums(nums):
  Counting = [0 for _ in range(3)]
  Sorting = []
  for i in nums: # for i un range(1,4): Counting.append(nums.count(i))
      Counting[i-1] += 1
  for i in range(3):
      Sorting.extend([i+1]*Counting[i])
  return Sorting
print (sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
