#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2022/12/27 11:52 PM
# Author  : xiaohui.wang
# File    : q1003_searchRotateArray.py
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
解题思路：二分查找，不过需要几个点：1、每次判断最左边是否是目标值
                               2、如果中间值等于目标值，不能直接返回，而是中间值作为右边界使用
                               3、如果中间值等于左边，或者等于右边，无法判断是否有序，则左边右移，右边左移
'''
#class Solution(object):
#    def search(self, arr, target):
#        """
#        :type arr: List[int]
#        :type target: int
#        :rtype: int
#        """
#        #try:
#        #    return arr.index(target)
#        #except:
#        #    return -1
#        end = len(arr) - 1
#        start = 0
#        mid = -1
#        while start <= end:
#            mid = (end - start) // 2 + start
#            if arr[mid] == target:
#                break
#            # 如果右边有序
#            if arr[mid] < arr[end]:
#                if arr[mid] <= target <= arr[end]:
#                    start = mid + 1
#                else:
#                    end = mid - 1
#            elif arr[mid] > arr[end]:
#                # 如果左边有序
#                if arr[start] <= target <= arr[mid]:
#                    end = mid - 1
#                else:
#                    start = mid + 1
#            else:
#                if arr[mid] == arr[end]:
#                    end = end -1
#                if arr[mid] == arr[start]:
#                    start = start + 1
#        if arr[mid] == target:
#            if mid == 0:
#                return mid
#            else:
#                if arr[mid-1] == target:
#                    while mid>=0 and arr[mid] == target:
#                        mid -= 1
#                    return mid + 1
#                else:
#                    if arr[0] == target:
#                        return 0
#                    else:
#                        return mid
#        else:
#            return -1
class Solution(object):
    def search(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        #try:
        #    return arr.index(target)
        #except:
        #    return -1
        end = len(arr) - 1
        start = 0
        while start <= end:
            #note1: 如果左边符合，直接返回，因为要找最小的索引
            if arr[start] == target:
                return start
            mid = (end - start) // 2 + start
            #note2: 如果中间值等于目标，不能直接返回结果，因为要找最小的索引，所以右边界等于中间值
            if arr[mid] == target:
                end = mid
            # 如果右边有序
            elif arr[mid] < arr[end]:
                if arr[mid] <= target <= arr[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            # 如果左边有序
            elif arr[mid] > arr[end]:
                if arr[start] <= target <= arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif arr[mid] == arr[end]:
                #note3: 如果中间值等于最后的值，且中间值等于开始的值，但是中间值不等于target
                # 右边左移，左边右移，这个时候时间复杂度会很差，相当于o(n)
                end -= 1
                if arr[mid] == arr[start]:
                    start = start + 1
        return -1


if __name__ == "__main__":
    soultion = Solution()
    nums1 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    res = soultion.search(nums1,5)
    print(res)
    nums1 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    res = soultion.search(nums1,11)
    print(res)
    nums1 = [15]
    res = soultion.search(nums1,15)
    print(res)
    nums1 = [1,1,1,1,1,2,1,1,1]
    res = soultion.search(nums1,2)
    print(res)
    nums1 = [5,5,5,1,2,3,4,5]
    res = soultion.search(nums1,5)
    print(res)
    nums1 = [12, 20, -21, -21, -19, -14, -11, -8, -8, -8, -6, -6, -4, -4, 0, 1, 5, 5, 6, 11, 11, 12]
    res = soultion.search(nums1,-8)
    print(res)
