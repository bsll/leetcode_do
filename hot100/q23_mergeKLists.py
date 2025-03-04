#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/25 16:37:57
# Author  : AI-NLP-WangXiaohui
# File    : q23_mergeKLists.py
'''
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
'''
'''
思路：顺序合并，每次合并两个
'''
from utils import ListNode,create_linked_list,print_linked_list

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        def mergeTwoLists(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            head = ListNode()
            l = head
            while l1 and l2:
                if l1.val <= l2.val:
                    l.next = l1
                    l1 = l1.next
                else:
                    l.next = l2
                    l2 = l2.next
                l = l.next
            l.next = l1 if l1 else l2
            return head.next
        ans = None
        n = len(lists)
        for i in range(len(lists)):
            ans = mergeTwoLists(ans,lists[i])
        return ans
if __name__ == "__main__":
    s = Solution()
    lis = [[1,4,5],[1,3,4],[2,6]]
    lis = [[2],[],[-1]]
    lists = []
    for i in range(len(lis)):
        lists.append(create_linked_list(lis[i]))
    print(print_linked_list(s.mergeKLists(lists)))
    


        


