#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/22 9:50 PM
# Author  : xiaohui.wang
# File    : isPalindrome_linklist.py
'''
给你一个单链表的头节点 head ，请你判断该链表是否为
回文链表
。如果是，返回 true ；否则，返回 false 。

 

示例 1：


输入：head = [1,2,2,1]
输出：true
示例 2：


输入：head = [1,2]
输出：false
 

提示：

链表中节点数目在范围[1, 105] 内
0 <= Node.val <= 9
'''
'''
解题思路：1、将链表转换为数组，然后判断数组是否为回文数组 s == s[::-1] ??
        2、将链表转换为字符串，然后判断字符串是否为回文字符串
'''
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        if res == res[::-1]:
            return True
        else:
            return False