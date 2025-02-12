#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/12 22:10:48
# Author  : AI-NLP-WangXiaohui
# File    : q39_combinationSum.py
'''
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

 

示例 1：

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []
 

提示：

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
candidates 的所有元素 互不相同
1 <= target <= 40
'''
'''
思路：
核心思路：回溯法 + 剪枝
排序候选数组：先将候选数组排序，便于后续剪枝和避免重复组合。
回溯函数设计：定义内部函数 back(i, cur_sum)，其中：
i 表示当前遍历的起始索引（控制元素选择范围）。
cur_sum 是当前组合的和。
递归终止条件：
若 cur_sum > target，直接返回（无效组合）。
若 cur_sum == target，将当前组合 state 的副本加入结果列表 res。
遍历候选元素：
从索引 i 开始遍历，允许重复选择同一元素（通过递归时传递 j 而非 j+1）。
将当前元素加入 state，递归尝试组合，回溯时弹出元素
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        candidates.sort()
        res = []
        state = []
        def back(i, cur_sum):
            if cur_sum > target:
                return
            elif cur_sum == target:
                res.append(state[:])
                return
            else:
                for j in range(i, n):
                    state.append(candidates[j])
                    back(j, cur_sum + candidates[j])
                    state.pop()
        back(0,0)
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,6,7],7))
                
