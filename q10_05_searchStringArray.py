#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2022/12/28 11:37 PM
# Author  : xiaohui.wang
# File    : q10_05_searchStringArray.py
'''
稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。

示例1:

 输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
 输出：-1
 说明: 不存在返回-1。
示例2:

 输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
 输出：4
提示:

words的长度在[1, 1000000]之间


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sparse-array-search-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
解题思路：1、直接用字典记住位置，然后返回，因为很少，所以空间复杂度低，时间复杂度o(n)
         2、二分查找，如果遇到空的时候，需要mid往左右找到有字母的边界，然后界定start和end的位置
'''
class Solution(object):
    def findString(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        start,end = 0, len(words)-1
        while start <= end:
            mid = (end-start)// 2 + start
            if  words[mid] == s:
                return mid
            if words[mid] == "":
                mid1 = mid
                mid2 = mid
                while words[mid1] == "" and mid1 > 0:
                    mid1 = mid1 -1
                while words[mid2] == "" and mid2 < len(words)-1:
                    mid2 = mid2 + 1
                if words[mid1] < s:
                    start = mid2 + 1
                elif words[mid1] > s:
                    end = mid1 - 1
                elif words[mid1] == s:
                    return mid1
                elif words[mid2] == s:
                    return mid2
            else:
                if words[mid] < s:
                    start = mid + 1
                else:
                    end = mid -1
        return -1
if __name__ == "__main__":
    soultion = Solution()
    words = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    s = "ta"
    res = soultion.findString(words,s)
    print(res)
    words = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    s = "ball"
    res = soultion.findString(words,s)
    print(res)
    words = ["DirNnILhARNS hOYIFB", "SM ", "YSPBaovrZBS", "evMMBOf", "mCrS", "oRJfjw gwuo", "xOpSEXvfI"]
    s = "mCrS"
    res = soultion.findString(words,s)
    print(res)
    words = ["CitZMIXZKoFbxvOlaza", "hBlKXdKJfBD"]
    s = "hBlKXdKJfBD"
    res = soultion.findString(words,s)
    print(res)
