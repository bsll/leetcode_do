#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/12/11 09:54:57
# Author  : AI-NLP-WangXiaohui
# File    : q24_swapPairs.py
'''
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]
'''
'''
思路：1、递归，依次交换相邻节点，直到节点为空，或者只有一个节点
     2、建一个虚拟节点作为中间节点，一直循环交换，直到节点为空或者只有一个节点
'''
from utils import ListNode,create_linked_list,print_linked_list

class Solution:
    def swapPairs(self, head):
        #递归终止条件是节点为空或者只有一个节点
        if not head or not head.next:
            return head
        #head是原始链表的头节点，也是新链表的第二个节点
        #newHead是新链表的头节点，也是原始链表的第二个节点
        #剩下的链表要用head.next 作为头节点
    
        #获取新的头节点（原来的头节点next就是新的头节点）
        newhead = head.next
        #交换完的节点接到老的头节点的后面
        head.next = self.swapPairs(newhead.next)
        #需要newhead 的next切断，换成原来的头节点
        newhead.next = head
        return newhead
if __name__ == '__main__':
    s = Solution()
    head = create_linked_list([1,2,3,4])
    print(print_linked_list(s.swapPairs(head)))
    head = create_linked_list([1])
    print(print_linked_list(s.swapPairs(head)))
    head = create_linked_list([])
    print(print_linked_list(s.swapPairs(head)))


