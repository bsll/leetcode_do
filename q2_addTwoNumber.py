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
解题思路：逐次累加，用头插法
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from hot100.utils import create_linked_list, print_linked_list, ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = end = ListNode(0)
        jinwei = 0
        while l1 or l2 :
            if not l1:
                l1_value = 0
            else:
                l1_value = l1.val
                l1 = l1.next
            if not l2:
                l2_value = 0
            else:
                l2_value = l2.val
                l2 = l2.next
            tmp = l1_value + l2_value + jinwei
            jinwei = 0
            if tmp >= 10:
                tmp_node = ListNode(tmp-10)
                jinwei = 1
            else:
                tmp_node = ListNode(tmp)
            end.next = tmp_node
            end = tmp_node
        if jinwei == 1:
            end.next = ListNode(jinwei)
        return head.next


if __name__ == "__main__":
    soultion = Solution()
    l1 = create_linked_list([9,9,9,9,9,9,9])
    l2 = create_linked_list([1])
    res = soultion.addTwoNumbers(l1,l2)
    print(print_linked_list(res))
    l1 = create_linked_list([2,4,3])
    l2 = create_linked_list([5,6,4])
    res = soultion.addTwoNumbers(l1,l2)
    print(print_linked_list(res))
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    res = soultion.addTwoNumbers(l1,l2)
    print(print_linked_list(res))
    l1 = create_linked_list([9,9,9,9,9,9,9])
    l2 = create_linked_list([9,9,9,9])
    res = soultion.addTwoNumbers(l1,l2)
    print(print_linked_list(res))
