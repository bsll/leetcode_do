#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/11 22:07:37
# Author  : AI-NLP-WangXiaohui
# File    : q46_permute.py
'''
 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

 

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
 
提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
'''
'''
思路：回溯法
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(cur):
            # 如果当前索引 cur 等于数组长度 n，说明找到一个排列
            if cur == n:
                res.append(nums[:])  # 将当前排列加入结果集
            # 遍历从 cur 到 n-1 的索引
            for i in range(cur, n):
                # 交换 nums[cur] 和 nums[i]，固定 nums[cur]
                nums[cur], nums[i] = nums[i], nums[cur]
                # 递归处理下一个位置
                backtrack(cur + 1)
                # 恢复交换（回溯）
                nums[cur], nums[i] = nums[i], nums[cur]

        n = len(nums)  # 数组长度
        res = []       # 存储所有排列的结果
        backtrack(0)   # 从索引 0 开始回溯
        return res     # 返回结果
if __name__ == "__main__":
    s = Solution()
    print(s.permute([1,2,3]))
    print(s.permute([0,1]))
    print(s.permute([1]))
