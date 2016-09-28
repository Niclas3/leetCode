class Solution(object):
  maxLength = 1000
  def longestPalindrome(self, s):
    lens = len(s)
    leftHand = ""
    rightHand = ""
    revRightHand = ""
    midIndex = lens / 2
    if lens % 2 == 0:
      leftHand = s[:midIndex]
      rightHand = s[midIndex:]
      revRightHand = rightHand[::-1]
#      print leftHand, revRightHand
    else:
      leftHand = s[:midIndex]
      rightHand = s[midIndex+1:len(s)]
      revRightHand = rightHand[::-1]
#      print leftHand, revRightHand 
    if leftHand == revRightHand:
      return True
    else:
      return False

so = Solution()
strs = "abccba"
#print len(strs)
print so.longestPalindrome(strs)
