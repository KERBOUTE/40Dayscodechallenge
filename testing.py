class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

  def pr(self,a=''):
      a=''
      a=str(self.val)+a
      m=self.next
      while m is not None:
          a=str(m.val)+a
          m = m.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.pr()
print(a)
