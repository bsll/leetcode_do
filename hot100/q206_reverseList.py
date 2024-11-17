#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/21 4:53 PM
# Author  : xiaohui.wang
# File    : reverseList.py
'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
 

示例 1：


输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：


输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]
 

提示：

链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000
'''
'''
解题思路：头插法
'''
from utils import ListNode,create_linked_list
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        res = None
        while head:
            tmp = ListNode(head.val)
            tmp.next = res
            res = tmp
            head = head.next
        return head
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        res = None
        while head:
            tmp = head.next
            head.next = res
            res = head
            head = tmp
        return res
    
if __name__ == '__main__':
    s = Solution()
    head = create_linked_list([1,2,3,4,5])
    print(s.reverseList(head))