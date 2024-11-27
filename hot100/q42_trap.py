#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/26 09:08:02
# Author  : AI-NLP-WangXiaohui
# File    : q42_trap.py
'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
'''
'''
思路：动态规划：1、建两个数组，一个从左往右依次变大，一个从右往左依次变大，
                这样就知道每个位置的左边的最大高度，和右边的最大高度
             2、找两个数组中的较小，减去当前的高度就是当前的蓄水量
                面积为两边的最大高度的较小值，减去本身的高度
     双指针：把动态规划里面的数组变成两个指针
'''
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        m = len(height)
        leftMax = [0] * m
        leftMax[0] = height[0]
        for i in range(1,m):
            leftMax[i] = max(leftMax[i-1], height[i])
        rightMax = [0] * m
        rightMax[-1] = height[-1]
        for i in range(m-2,-1,-1):
            rightMax[i] = max(height[i], rightMax[i+1])
        area = 0
        for i in range(m):
            area = area + min(leftMax[i],rightMax[i]) - height[i]
        return area
    def trap2(self, height: List[int]) -> int:
        m = len(height)
        left = 0
        right = m-1
        leftMax = 0
        rightMax = 0
        area = 0
        while left < right:
            leftMax = max(leftMax,height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                area = area + leftMax - height[left]
                left += 1
            elif height[left] >= height[right]:
                area = area + rightMax - height[right]
                right -= 1
        return area
if __name__ == "__main__":
    s = Solution()
    print(s.trap2([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(s.trap2([4,2,0,3,2,5]))
                   
            


            

