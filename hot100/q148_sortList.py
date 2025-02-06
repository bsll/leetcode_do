#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/06 08:11:05
# Author  : AI-NLP-WangXiaohui
# File    : q148_sortList.py
'''
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

示例 1：

输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：

输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：

输入：head = []
输出：[]
 
提示：

链表中节点的数目在范围 [0, 5 * 10^4] 内
-10^5 <= Node.val <= 10^5
'''
'''
思路：归并排序
先找到链表的中点（快慢指针），然后对两边排序，排序完之后合并两个有序链表
分治：将链表递归地分成两半，直到每个子链表只剩一个节点（自然有序）。
合并：将两个有序子链表合并为一个有序链表。
'''
from utils import ListNode,create_linked_list,print_linked_list
class Solution:
    def sortList(self, head):
        def split(head, tail):
            #如果节点为None,直接返回
            if not head:
                return head
            #如果只剩下最后一个节点，需要将链表断开，直接返回
            if head.next == tail:
                head.next = None
                return head
            fast = head
            slow = head
            #快慢指针找中点
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:  #不相等是，fast 多走一步
                    fast = fast.next
            mid = slow
            #递归分割并合并
            return merge(split(head,mid), split(mid,tail))
        def merge(head1, head2):
            if not head1:
                return head2
            if not head2:
                return head1
            #使用虚拟头节点，所以返回 head.next
            head = ListNode(0)
            l = head
            while head1 and head2: #比较并链接较小的节点
                if head1.val <= head2.val:
                    l.next = head1
                    head1 = head1.next
                else:
                    l.next = head2
                    head2 = head2.next
                l = l.next
            #处理剩余的部分
            l.next = head1 if head1 else head2
            return head.next
        #初始 tail为 None节点
        return split(head,None)
if __name__ == '__main__':
    s = Solution()
    head = create_linked_list([4,2,1,3])
    print(print_linked_list(s.sortList(head)))
    head = create_linked_list([-1,5,3,4,0])
    print(print_linked_list(s.sortList(head)))
    head = create_linked_list([])
    print(print_linked_list(s.sortList(head)))
    

        


