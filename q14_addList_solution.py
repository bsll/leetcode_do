#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2022/12/21 9:14 PM
# Author  : xiaohui.wang
# File    : Solution.py
'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
https://leetcode.cn/problems/longest-common-prefix/
依次遍历，提前退出
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_str = ""
        if len(strs) == 0:
            return common_str
        if len(strs) == 1:
            return strs[0]
        len1, len2 = len(strs[0]), len(strs[1])
        j = 0
        while j < len1 and j < len2:
            if strs[0][j] == strs[1][j]:
                common_str += strs[0][j]
                j += 1
            else:
                break
        if len(strs) == 2:
            return common_str
        else:
            cur_common = common_str
        if cur_common == "":
            return cur_common
        for i in range(2,len(strs)):
            len1,len2 = len(cur_common),len(strs[i])
            tmp_common = ""
            j = 0
            while j < len1 and j < len2:
                if cur_common[j] == strs[i][j]:
                    tmp_common += strs[i][j]
                    j += 1
                else:
                    break
            cur_common = tmp_common
            if cur_common == "":
                break
        return cur_common

if __name__ == "__main__":
    soultion = Solution()
    strs = ["flower", "flow", "flight"]
    print(soultion.longestCommonPrefix(strs))
    strs = ["dog", "racecar", "car"]
    print(soultion.longestCommonPrefix(strs))
    strs = ["a","a","b"]
    print(soultion.longestCommonPrefix(strs))



