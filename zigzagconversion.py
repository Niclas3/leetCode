class Solution(object):
  def convert(self, s, numRows):
    arr = []
    for index, c in enumerate(s):
      print index, c


so = Solution()
s = "ABCDEFJHIJK"
row = 3
print so.convert(s, row)
