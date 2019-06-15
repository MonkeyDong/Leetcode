# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def prints(head):
	arrs = []
	while(head != None):
		arrs.append(head.val)
		head = head.next
	r = []
	for i in arrs:
		r.append(str(i))
	strs = '->'.join(r)
	print(strs)

class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		if head == None or head.next == None:
			return head
		arr = []
		while(head):
			arr.append(head.val)
			head = head.next
		res = ListNode(arr.pop())
		t = res
		while(arr != []):
			res.next = ListNode(arr.pop())
			res = res.next
		return t

	def NewNode(self,lists):
		n = ListNode(lists[0])
		t = n
		for i in lists[1:]:
			n.next = ListNode(i)
			n = n.next
		return t


lists = [1,2,3,4,5]
test = Solution()
lis = test.NewNode(lists)
prints(lis)
res = test.reverseList(lis)
prints(res)



