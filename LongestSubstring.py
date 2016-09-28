# Longest SubString Without Repeating Characters

class Solution(object):
  def lengthOfLongestSubstring(self, s):
    print s
    print self.getSubStringStartChart(s)

  def findSubString(self, s):
    index = self.getSubStringStartChart(s)
    pass

  def getSubStringStartChart(self, s):
    dic = {}
    firstWord = ""
    if len(s) > 0:
      firstWord = s[0]
    else:
      pass

    for index, c in enumerate(s):
      if not dic.has_key(c):
        #print "+", c, index
        dic[c] = index
      else:
        firstWord = c
        return index
    return 0

strs = "abcabcabcd"
so = Solution()
so.lengthOfLongestSubstring(strs)
