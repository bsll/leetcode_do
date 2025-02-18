#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/18 16:54:43
# Author  : AI-NLP-WangXiaohui
# File    : q347_topKFrequent.py
'''
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
 

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
'''
'''
思路： 1、直接暴力排序，然后取数
      2、利用哈希表统计数目，利用二维列表存每个位置对应的元素，从大到小遍历，把不为空且大于 k 的合并返回
'''
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res1 = collections.defaultdict(int)
        for num in nums:
            res1[num] += 1
        res2 = [[] for _ in range(len(nums) + 1)]
        for item in res1:
            res2[res1[item]].append(item)
        print(res2)
        res = []
        for i in range(len(res2)-1,0,-1):
            if len(res2[i]) != 0:
                if k > 0:
                    res += res2[i]
                    k -= len(res2[i])
        return res
if __name__ == "__main__":
    s = Solution()
    nums = [4,1,-1,2,-1,2,3]
    k = 2
    print(s.topKFrequent(nums,k))
    nums = [1]
    k = 1
    print(s.topKFrequent(nums,k))
    nums = [1,2]
    k = 2
    print(s.topKFrequent(nums,k))


    
        
        
        