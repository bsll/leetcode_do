#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/20 08:58:02
# Author  : AI-NLP-WangXiaohui
# File    : q121_maxProfit.py
'''
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
'''
'''
思路：动态规划 maxProfit[i] = max(Profit[i-1], prices[i] - min(prices[0:i]))
每次求min会超出时间限制，所以用一个变量来记录最小值
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxsale = 0
        if len(prices) == 0:
            return maxsale
        currentMin = prices[0]
        for i in range(1,len(prices)):
            maxsale = max(maxsale, prices[i] - currentMin)
            if prices[i] < currentMin:
                currentMin = prices[i]
        return maxsale
if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))
