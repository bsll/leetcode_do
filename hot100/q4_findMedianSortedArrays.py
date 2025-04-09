#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/03/14 13:02:28
# Author  : AI-NLP-WangXiaohui
# File    : q4_findMedianSortedArrays.py
'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
 
提示：
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''
'''
思路:
两个有序数组的中位数可转化为求第k小元素的问题。若总长度m+n为奇数，中位数为第(m+n+1)//2小的元素；若为偶数，则为第(m+n)//2和第(m+n)//2+1小元素的平均值。

每次排除不可能包含第k小元素的部分。比较两个数组的第k/2个元素，较小的部分的前k/2个元素不可能为第k小元素，可跳过这些元素并更新k的值。

递归排除：通过不断调整数组的起始索引和k值，逐步缩小搜索范围，直到找到目标元素。

'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def getKthElement(k):
            index1, index2 = 0,0
            while True:
                #如果数组1遍历完了，返回数组2剩下的第k-1个元素
                if index1 == m:
                    return nums2[index2 + k - 1]
                #同理，如果数组2遍历完了，返回数组1剩下的第k-1个元素
                if index2 == n:
                    return nums1[index1 + k - 1]
                #如果 k=1,就返回两个数组当前索引中的较小值，此时剩下的最小的那个就是第k个
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                #通过min函数确保索引不越界(m-1,n-1)，计算两个数组中第k/2个元素的位置。
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                #比较两个数组的pivot值，排除较小pivot所在数组的前k/2个元素，更新索引和k值，继续循环。
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                #如果pivot1小于等于pivot2，说明nums1的前半部分肯定都在第k小元素的前面，所以可以跳过这些元素
                if pivot1 <= pivot2:
                    # k 减去被跳过的元素的数量
                    k = k - (newIndex1 - index1 + 1)
                    # 更新索引
                    index1 = newIndex1 + 1
                else:
                    k = k - (newIndex2 - index2 + 1)
                    index2 = newIndex2+ 1
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        # 奇数和偶数的不同处理
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

if __name__ == "__main__":
    s = Solution()
    nums1 = [1,3]
    nums2 = [2]
    print(s.findMedianSortedArrays(nums1, nums2))
    nums1 = [1,2]
    nums2 = [3,4]
    print(s.findMedianSortedArrays(nums1, nums2))

                
