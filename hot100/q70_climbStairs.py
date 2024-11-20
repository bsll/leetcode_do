#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/20 09:27:11
# Author  : AI-NLP-WangXiaohui
# File    : q70_climbStairs.py
'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

 

示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
'''
'''
思路：1、斐波那契数列 f(n) = f(n-1) + f(n-2)
     2、空间复杂度更高的动态规划，dp[i] = dp[i-1] + dp[i-2]
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=2:
            return n
        res1 = 1
        res2 = 2
        for i in range(3,n+1):
            res3 = res1 + res2
            res1 = res2
            res2 = res3
        return res3
if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
    print(s.climbStairs(2))
