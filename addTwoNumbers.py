# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, nextList):
        self.val = x
        self.next = nextList 

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    num1 = self.list2Number(l1)
    num2 = self.list2Number(l2)
    nums = num1 + num2
    print num1,"+", num2, "=",nums

    print self.number2List(nums)
    return nums
    #return self.number2List(nums)

  def lenListNode(self, lists):
    count = 1
    lst = lists
    while lst.next != None:
      lst = lst.next
      count += 1
    return count

  def list2Number(self, lists):
    length = self.lenListNode(lists)
    res = 0
    lst = lists
    index = 0
    while lst != None:
      res += (lst.val * pow(10, index))
      index += 1
      lst = lst.next
    return res

  def number2List(self, num):
    if num < 10:
      return [num]
    res = num
    count = 0
    while True:
      res = res/ 10
      count += 1
      if res < 1:
        break
      else:
        pass
    lst = []
    resLst = num
    for index in range(1, count):
      digit = resLst % pow(10, index)
      resLst -= digit
      digit = digit / pow(10, index-1)
      lst.append(digit)
      if index == count-1:
        lst.append(resLst/pow(10, index))
    return lst

#l3 = ListNode(3, None)
#l2 = ListNode(4, l3)
l1 = ListNode(0, None)

#l6 = ListNode(4, None)
#l5 = ListNode(6, l6)
l4 = ListNode(1, None)

so = Solution()
so.addTwoNumbers(l1, l4)
