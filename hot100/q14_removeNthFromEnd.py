#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/28 10:47 PM
# Author  : xiaohui.wang
# File    : removeNthFromEnd.py
'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

 
示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]
 

提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

'''
'''
解题思路：快慢指针，两个隔着n步开始走，一个到头了，另外一个就在 n 的位置了
'''

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        low = head
        i = 0
        while i < n:
            fast = fast.next
            i += 1
        while fast != None and fast.next != None:
            fast = fast.next
            low = low.next
        if fast == None:
            return head.next
        else:
            low.next = low.next.next
            return head