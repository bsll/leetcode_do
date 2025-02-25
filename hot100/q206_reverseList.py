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
每次处理一个节点，将当前节点的next指向前一个节点（即新链表的头），然后更新头节点为当前节点，最后移动当前节点到原链表的下一个节点
'''
from utils import ListNode,create_linked_list,print_linked_list
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
    def reverseList3(self, root):
        if not root:
            return root
        head = None
        while root:
            #临时保存下一个节点，防止后续修改 root.next 后丢失原来链表后续节点
            tmp = root.next
            #反转指针方向，当前节点的next指向新链表的头部（即前一个节点）
            root.next = head
            #更新新链表头部
            head = root
            #移动到原链表下一个节点
            root = tmp
        return head
    
if __name__ == '__main__':
    s = Solution()
    head = create_linked_list([1,2,3,4,5])
    print(print_linked_list(s.reverseList3(head)))