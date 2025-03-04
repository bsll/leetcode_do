#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/21 4:57 PM
# Author  : xiaohui.wang
# File    : mergeTwoLists.py
'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]
 

提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
'''
'''
解题思路：同时遍历两个链表，比较大小，将小的节点放到新链表中
'''
from utils import ListNode,create_linked_list,print_linked_list
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode()
        l = head
        while l1 and l2:
            if l1.val >= l2.val:
                l.next = l2
                l2 = l2.next
            else:
                l.next = l1
                l1 = l1.next
            l = l.next
        l.next = l1 if l1 else l2
        return head.next
    #递归的方法
    def mergeTwoLists1(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        l2.next = self.mergeTwoLists(l1,l2.next)
        return l2

if __name__ == "__main__":
    s = Solution()
    l1 = [1,2,4]
    l2 = [1,3,4]
    print(print_linked_list(s.mergeTwoLists(create_linked_list(l1),create_linked_list(l2))))
