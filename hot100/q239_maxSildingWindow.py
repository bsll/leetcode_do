#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/29 09:46:50
# Author  : AI-NLP-WangXiaohui
# File    : q239_maxSildingWindow.py
'''
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

 

示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：

输入：nums = [1], k = 1
输出：[1]
'''
'''
思路： 1、暴力求解,时间会超时
         找到当前滑动窗口的最大值，然后在滑动的时候比较出去和进来的值与最大值的关系
         如果出去和进来的都比最大值小，则最大值不变
         如果出去的等于最大值，则需要重新寻找最大值
         如果进来的比最大值大，则更新最大值
      2、单调队列
      #如果队列头部的元素已经不在窗口中，左移除，最后添加
            while q[0] <= i-k:
                q.popleft()
       
'''
import collections
from typing import List
class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        m = len(nums)
        max_arr = []
        cur_max = max(nums[:k])
        max_arr.append(cur_max)
        for i in range(1,m-k+1):
            if nums[i-1] < cur_max and nums[i+k-1] < cur_max:
                max_arr.append(cur_max)
            elif nums[i-1] == cur_max:
                cur_max = max(nums[i:i+k])
                max_arr.append(cur_max)
            elif nums[i+k-1] >= cur_max:
                cur_max = nums[i+k-1]
                max_arr.append(cur_max)
        return max_arr

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        m = len(nums)
        max_arr = []
        for i in range(m-k+1):
            max_arr.append(max(nums[i:i+k]))
        return max_arr

    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        #使用双端队列构造单调队列，用来存储滑动窗口内的元素索引
        q = collections.deque()
        for i in range(k):
            #移除队列中所有小于当前元素的元素的索引，并把当前索引加到队列中
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        #初始窗口最大值就是索引最小的那个元素的值
        ans = [nums[q[0]]]
        for i in range(k,n):
            #移除队列中所有小于当前元素的元素的索引，并把当前索引加到队列中
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            #如果队列头部的元素已经不在窗口中，左移除，最后添加
            while q[0] <= i-k:
                q.popleft()
            ans.append(nums[q[0]])
        return ans

if __name__ == "__main__":
    s = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(s.maxSlidingWindow(nums,k))
    nums = [1]
    k = 1
    print(s.maxSlidingWindow(nums,k))
            