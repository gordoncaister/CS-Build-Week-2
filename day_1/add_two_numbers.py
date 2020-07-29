# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = ""
        list2 = ""
        while l1:
            list1 = "".join(str(l1.val)) + list1
            l1 = l1.next
            
        while l2:
            list2 = "".join(str(l2.val)) + list2
            l2 = l2.next
            
        strlist = list(str(int(list1)+int(list2)))
        l3 = ListNode(int(strlist[0]))
        for j in range(1,len(strlist)):   
            l3 = ListNode(int(strlist[j]),l3)

        return(l3)