#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/03/14 08:52:38
# Author  : AI-NLP-WangXiaohui
# File    : q84_largestRectangleArea.py
'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例 1:
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：

输入： heights = [2,4]
输出： 4

提示：
1 <= heights.length <=105
0 <= heights[i] <= 104
'''
'''
思路：
单调栈：栈中保存索引，对应的高度保持递增。遇到较小元素时，栈顶元素的右边界确定为当前索引，同时更新其左边界。

边界处理：对于每个柱子，左边界为栈中前一个元素（或-1），右边界为第一个比它小的元素位置（或n）。

面积计算：每个柱子的最大矩形面积为高度乘以宽度（右边界 - 左边界 - 1）。

对于每个柱子i，找到左边第一个比它矮的柱子的位置，记录在left[i]中，
右边第一个比它矮的柱子的位置记录在right[i]中。
这样，当前柱子所能形成的最大矩形的宽度就是right[i] - left[i] -1，
然后乘以当前柱子的高度，得到面积。然后取最大的面积就是答案。


'''
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n <= 0:
            return 0
        # 左侧第一个比当前小的索引值
        left = [0] *n
        # 右侧第一个比当前小的索引值，初始化为n
        right = [n] * n
        # 栈里面存的是索引值
        stack = []
        for i in range(n):
            # 弹出栈顶元素直到栈顶元素小于当前高度
            #
            #
            while stack and heights[stack[-1]] >= heights[i]:
                # 当前i是被弹出元素的右侧第一个更小元素
                #
                #
                right[stack[-1]] = i
                stack.pop()
            # 更新当前元素的左边界
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            # 切记：需要把最新的i加上去
            #
            #
            stack.append(i)
        ans = 0
        for i in range(n):
             # 计算以heights[i]为高的最大矩形面积
            ans = max(ans,(right[i]-left[i]-1) * heights[i])
        return ans
if __name__ == "__main__":
    s = Solution()
    heights = [2,1,5,6,2,3]
    print(s.largestRectangleArea(heights))
    heights = [2,4]
    print(s.largestRectangleArea(heights))


