#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/10 3:27 PM
# Author  : xiaohui.wang
# File    : coinChange.py
'''
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
'''
'''
思路：动态规划 f(n) = min(f(n-c)) + 1,c为coins中的上一个元素
核心是计算每一个金额所需要的最小金币个数，然后依次计算，直到计算到目标金额
'''
class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        dp = [0] * (amount+1)
        i = 1
        while i <= amount:
            minvalue = 100000
            # 依次用所有的硬币金额去匹配
            for j in range(len(coins)):
                # 如果当前金额减去硬币金额大于0，则说明可以减去该硬币
                if i - coins[j] >= 0:
                    # 如果 dp[i-coins[j]] 不等于-1,说明dp[i-coins[j]]有值，则可以计算当前的最小值
                    # 每一次计算都是基于上一个元素计算出来的
                    if dp[i-coins[j]] != -1:
                        minvalue = min(minvalue,dp[i-coins[j]])
            if minvalue != 100000:
                dp[i] = minvalue + 1
            else:
                dp[i] = -1
            i += 1
        return dp[-1]
if __name__ == "__main__":
    s = Solution()
    coins = [1,2,5]
    amount = 11
    print(s.coinChange(coins, amount))
    coins = [1]
    amount = 2
    print(s.coinChange(coins, amount))
    coins = [1]
    amount = 0
    print(s.coinChange(coins, amount))






