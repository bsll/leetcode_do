#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/25 16:19:51
# Author  : AI-NLP-WangXiaohui
# File    : q25_reverseKGroup.py
'''
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

 示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
示例 2：



输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
 

提示：
链表中的节点数目为 n
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
'''
'''
思路：每次取 K 个元素，进行反转链表
'''
from utils import ListNode,create_linked_list,print_linked_list

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def reverse(head,tail):
            prev = tail.next
            p = head
            while prev != tail:
                tmp = p.next
                p.next = prev
                prev = p
                p = tmp
            return tail,head
        vir_head = ListNode(0)
        vir_head.next = head
        pre = vir_head
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return vir_head.next
            tmp = tail.next
            head, tail = reverse(head,tail)
            pre.next = head
            tail.next = tmp
            pre = tail
            head = tail.next
        return vir_head.next
    
if __name__ == "__main__":
    s = Solution()
    head = [1,2,3,4,5]
    k = 2
    print(print_linked_list(s.reverseKGroup(create_linked_list(head),k)))
        



