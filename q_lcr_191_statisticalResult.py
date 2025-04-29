#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/04/23 09:02:40
# Author  : AI-NLP-WangXiaohui
# File    : q191_statisticalResult.py
'''
为了深入了解这些生物群体的生态特征，你们进行了大量的实地观察和数据采集。数组 arrayA 记录了各个生物群体数量数据，其中 arrayA[i] 表示第 i 个生物群体的数量。请返回一个数组 arrayB，该数组为基于数组 arrayA 中的数据计算得出的结果，其中 arrayB[i] 表示将第 i 个生物群体的数量从总体中排除后的其他数量的乘积。

 

示例 1：

输入：arrayA = [2, 4, 6, 8, 10]
输出：[1920, 960, 640, 480, 384]
 

提示：

所有元素乘积之和不会溢出 32 位整数
arrayA.length <= 100000

'''
'''
思路：1、暴力法 会超时
     2、计算前缀积和后缀积，然后两个相乘
    i 0 1 2 3 4
a 1 2 3 4 5 

b0 = 1
b1 = b0 * a0 = a0
b2 = b1 * a1 = a0 * a1
b3 = b2 * a2 = a0 * a1 * a2
b4 = b3 * a3 = a0 * a1 * a2 * a3

tmp = a4;                      b3 = b3 * a4                = a0 * a1 * a2 * a4 
tmp = a4 * a3;                 b2 = b2 * a4 * a3           = a0 * a1 * a3 * a4 
tmp = a4 * a3 * a2;            b1 = b1 * a4 * a3 * a2      = a0 * a2 * a3 * a4  
tmp = a4 * a3 * a2 * a1;       b0 = b0 * a4 * a3 * a2 * a1 = a1 * a2 * a3 * a4  
'''
class Solution(object):
    def statisticalResult(self, a):
        """
        :type arrayA: List[int]
        :rtype: List[int]
        这种比较好理解
        """
        m = len(a)
        b = [1] * m 
        # 计算前缀积
        left = 1
        for i in range(m):
            b[i] = left
            left = left * a[i]
        # 计算后缀积
        right = 1
        for i in range(m-1, -1, -1):
            b[i] *= right
            right = right * a[i]
        return b
    def statisticalResult1(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        m = len(a)
        b = [1] * m
        tmp = 1
        for i in range(1,m):
            b[i] = b[i-1] * a[i-1]  # 下三角
        for i in range(m-2,-1,-1):
            tmp *= a[i+1]    #上三角
            b[i] *= tmp
        return b
if __name__ == "__main__":
    s = Solution()
    a = [2, 4, 6, 8, 10]
    print(s.statisticalResult(a))
    print(s.statisticalResult1(a))
