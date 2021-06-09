#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/6/9 9:57 PM
# Author  : xiaohui.wang
# File    : Solution.py
'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
解题思路：
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = []
        len1 = len(l1)
        len2 = len(l2)
        i = 0
        jinwei = 0
        while i < len1 or i < len2:
            if i >= len1:
                l1_value = 0
            else:
                l1_value = l1[i]
            if i >= len2:
                l2_value = 0
            else:
                l2_value = l2[i]
            tmp = l1_value + l2_value + jinwei
            if tmp >= 10:
                l3.append(tmp - 10)
                jinwei = 1
            else:
                l3.append(tmp)
            i += 1
        if jinwei == 1:
            l3.append(jinwei)
        return l3




if __name__ == "__main__":
    soultion = Solution()
    l1 = [9,9,9,9,9,9,9]
    l2 = [1]
    res = soultion.addTwoNumbers(l1,l2)
    print(res)