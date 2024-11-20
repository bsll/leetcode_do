#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/5 9:24 PM
# Author  : xiaohui.wang
#  File    : dailyTemperatures.py
'''
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

 

示例 1:

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
示例 2:

输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
示例 3:

输入: temperatures = [30,60,90]
输出: [1,1,0]
'''
'''
思路: 用栈实现，如果栈为空，直接入栈，
如果栈不为空，比较栈顶元素和当前元素，
    如果当前元素大于栈顶元素，说明找到了，弹出栈顶元素，并计算距离，
    如果当前元素小于栈顶元素，然后将当前元素入栈
'''
class Solution(object):
    def dailyTemperatures(self, temperatures):
        m = len(temperatures)
        dist = [0 for _ in range(m)]
        tmp = []
        for i in range(0,m):
            #永远让栈保持递减，如果不满足了，就弹出赋值，因为说明找到了
            while tmp != [] and temperatures[i] > temperatures[tmp[-1]]:
                dist[tmp[-1]] = i - tmp[-1]
                tmp.pop()
            tmp.append(i)
        return dist
if __name__ == "__main__":
    s = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print(s.dailyTemperatures(temperatures))
    temperatures = [30,30,30]
    print(s.dailyTemperatures(temperatures))

