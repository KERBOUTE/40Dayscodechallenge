class Solution:

  def lengthOfLongestSubstringFistmethod(self, s):
    list = sorted([(i,j) for i,j in enumerate(s)], key=lambda tup: tup[1])
    list =sorted([list[i] for i in range(len(list)-1) if list[i][1]==list[i+1][1] and list[i][0]==list[i+1][0]-1], key=lambda tup: tup[0])
    x=0
    for i in range(len(list)-1):
        if list[i+1][0]-list[i][0]>x:
            x=list[i+1][0]-list[i][0]
    return x

  def lengthOfLongestSubstringSecondmethod(self, s):
    ss=' '+s  # ' abrkaabcdefghijjxxx'
    s=s+' '   # 'abrkaabcdefghijjxxx '
    x=0
    for i in range(len(s)):
        if s[i]==ss[i] and i-x > x:
            x=i-x
    return x

print(Solution().lengthOfLongestSubstringFistmethod('abrkaabcdefghijjxxx'))
print(Solution().lengthOfLongestSubstringSecondmethod('abrkaabcdefghijjxxx'))
# 10
