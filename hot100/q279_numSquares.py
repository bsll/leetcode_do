#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/9 11:08 PM
# Author  : xiaohui.wang
# File    : numSquares.py
'''
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。


示例 1：

输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9
'''
'''
思路：f(n) = min(currmin, f(n-i*i)) + 1  其中i*i <= n,至少需要 1 个，即它本身
'''
class Solution(object):
    def numSquares(self, n):
        #要找到是去掉当前一个平方数，之后找到该数需要的最小元素个数
        f = [0] * (n + 1)
        f[0] = 0
        for i in range(1,n+1):
            j = 1
            minvalue = 100000
            while j * j <= i:
                minvalue = min(minvalue, f[i-j*j])
                j += 1
            f[i] = 1 + minvalue
        return f[n]
if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(12))
    print(s.numSquares(13))
    print(s.numSquares(16))


