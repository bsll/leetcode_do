#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/12/03 09:03:19
# Author  : AI-NLP-WangXiaohui
# File    : q56_merge.py
'''
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

 

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

'''
'''
注意：数组不是完全递增的
思路：先排序，然后按照区间对比去找就行了
'''
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        m = len(intervals)
        if m == 0:
            return []
        if m == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res = []
        merge_res = [intervals[0][0],intervals[0][1]]
        for i in range(1,m):
            start1 = intervals[i][0]
            end1 = intervals[i][1]
            if start1 <= merge_res[1]:
                merge_res = [merge_res[0],max(merge_res[1],end1)]
            else:
                res.append(merge_res)
                merge_res = [start1,end1]
        res.append(merge_res)
        return res


if __name__ == "__main__":
    s = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(s.merge(intervals))
    intervals = [[1,4],[4,5]]
    print(s.merge(intervals))
    intervals = [[1,4],[0,4]]
    print(s.merge(intervals))
    intervals = [[1,4],[0,0]]
    print(s.merge(intervals))

