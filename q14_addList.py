#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2022/12/21 9:14 PM
# Author  : xiaohui.wang
# File    : Solution.py
'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
 

提示：

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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



