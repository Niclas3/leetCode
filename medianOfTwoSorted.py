class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    lst = nums1
    lst.extend(nums2)
    lst.sort()
    print lst
    print len(lst)

    if not len(lst) % 2 == 0:
      return lst[len(lst)/2]
    else :
      twoNum = lst[len(lst)/2 - 1:len(lst)/2+1]
      print twoNum
      sum = reduce(lambda x, y: x+y, twoNum)
      res = sum / 2.0
      return res

so = Solution()
nums1 = [1,3,5,5,5,53,2,4,23,4,234,23,4,23,4,234,23,4,23,4,23,423,4,23,5,3,254,1,234]
nums2 = [2]

print so.findMedianSortedArrays(nums1, nums2)
