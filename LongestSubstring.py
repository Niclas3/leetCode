# Longest SubString Without Repeating Characters

class Solution(object):
  def lengthOfLongestSubstring(self, s):
    print self.getSubStringStartChart(s)
   #  strs = s[2:]
   # print self.getSubStringStartChart(strs)
   # strss = strs[3:]
   # print self.getSubStringStartChart(strss)

  def getSubStringStartChart(self, s):
    dic = {}
    firstWord = ""
    if len(s) > 0:
      firstWord = s[0]
    else:
      pass

    for index, c in enumerate(s):
      if not dic.has_key(c):
        print "+", c, index
        dic[c] = index
      else:
        firstWord = c
        return (index, firstWord)
    return (0, firstWord)

strs = "bbbbbbbb"
so = Solution()
so.lengthOfLongestSubstring(strs)
