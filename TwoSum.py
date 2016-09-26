class Solution(object):
  def twoSum(self, nums, target):
    for i in range(len(nums)):
      temp = nums[i]
      for j in range(i+1, len(nums)):
        tempTwo = nums[j]
        if (temp + tempTwo) == target:
          return [i, j]
    return None

so = Solution()
nums = [3, 10, 1, 7, 11, 9, 2, 4 ];
target = 6;
print so.twoSum(nums, target)
