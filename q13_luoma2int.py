#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2022/12/22 10:38 PM
# Author  : xiaohui.wang
# File    : q3_luoma2int.py
'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
解题思路：除了I以外2个2个的看，根据左右的位置做加减法？
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = {'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        if len(s) == 1:
            return nums[s]
        res = nums[s[0]]
        for i in range(1,len(s)):
            if (s[i-1] == 'I' and s[i] in ["X","V"]) \
                or (s[i-1] == "X" and s[i] in ["L",'C'])\
                   or (s[i-1] == "C" and s[i] in ["D","M"]):
                res += (nums[s[i]] - 2 * nums[s[i-1]])
            else:
                res += nums[s[i]]
        return res





if __name__ == "__main__":
    soultion = Solution()
    s = "MCMXCIV"
    res = soultion.romanToInt(s)
    print(res)
    s = "LVIII"
    res = soultion.romanToInt(s)
    print(res)
    s = "IX"
    res = soultion.romanToInt(s)
    print(res)
    s = "IV"
    res = soultion.romanToInt(s)
    print(res)
    s = "III"
    res = soultion.romanToInt(s)
    print(res)
