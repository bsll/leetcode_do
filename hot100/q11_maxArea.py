#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/25 09:02:07
# Author  : AI-NLP-WangXiaohui
# File    : q11_maxArea.py
'''
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1
'''
'''
思路：双指针，一个从前面找，一个从最后面找，每次从短的往长的移动
     这个题要记住的是，要找两个线能接的最多的水，不是两个线范围内能接的最多水。
'''
class Solution(object):
    def maxArea(self,height):
        if len(height) <= 1:
            return 0
        maxArea = 0
        start = 0
        end = len(height) - 1
        while start < end:
            if height[start] >= height[end]:
                maxArea = max(maxArea, height[end] * (end-start))
                end -= 1
            else:
                maxArea = max(maxArea, height[start] * (end-start))
                start += 1
        return maxArea
if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    print(s.maxArea([1,1]))
    print(s.maxArea([1]))
    print(s.maxArea([]))





