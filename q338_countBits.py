#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/04/24 09:34:04
# Author  : AI-NLP-WangXiaohui
# File    : q_lcr_003_countBits.py
'''
给定一个非负整数 n ，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。

 

示例 1:

输入: n = 2
输出: [0,1,1]
解释: 
0 --> 0
1 --> 1
2 --> 10
示例 2:

输入: n = 5
输出: [0,1,1,2,1,2]
解释:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

说明 :

0 <= n <= 105
 

进阶:

给出时间复杂度为 O(n*sizeof(integer)) 的解答非常容易。但你可以在线性时间 O(n) 内用一趟扫描做到吗？
要求算法的空间复杂度为 O(n) 。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount ）来执行此操作。
'''
'''
思路：利用 n = n & n-1 每次会消除一个 1，直到 n = 0
'''
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def countn(n):
            count = 0
            while n != 0:
                n = n & (n-1)
                count += 1
            return count
        res = []
        for i in range(0,n+1):
            res.append(countn(i))
        return res
if __name__ == "__main__":
    sou = Solution()
    n = 5
    print(sou.countBits(n))
