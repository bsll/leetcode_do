#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2022/12/22 9:28 PM
# Author  : xiaohui.wang
# File    : q1138_charPath.py
'''
我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。

在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下所示。



我们可以按下面的指令规则行动：

如果方格存在，'U' 意味着将我们的位置上移一行；
如果方格存在，'D' 意味着将我们的位置下移一行；
如果方格存在，'L' 意味着将我们的位置左移一列；
如果方格存在，'R' 意味着将我们的位置右移一列；
'!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。
（注意，字母板上只存在有字母的位置。）

返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/alphabet-board-path
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
题目思路:把每个字符对应的位置映射存下来，然后根据坐标，判断上下左右，字母Z可能需要特殊处理
常规思路：其他字母到Z,先左右后上下
Z到其他字母,先上下后左右
当成越界问题考虑

优化思路：
无论哪种情况，一招上左下右的顺序移动就可以
'''
class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        #board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        #res = {}
        #for key in range(len(board)):
        #    for item in range(len(board[key])):
        #        res[board[key][item]] = (key,item)
        res = {}
        for i in range(26):
            res[chr(i+97)] = (i//5,i%5)
        cur_j = 0
        cur_i = 0
        path = ""
        for char in target:
            target_i,target_j = res[char]
            while target_i < cur_i:
                path += 'U'
                cur_i -= 1
            while target_j < cur_j:
                path += 'L'
                cur_j -= 1
            while target_i > cur_i:
                path += 'D'
                cur_i += 1
            while target_j > cur_j:
                path += "R"
                cur_j += 1
            path += '!'
        return path
        #res = {}
        #for i in range(26):
        #    res[chr(i+97)] = (i//5,i%5)
        #cur_i = 0
        #cur_j = 0
        #path = ""
        #for char in target:
        #    target_i,target_j = res[char]
        #    dx = target_i - cur_i
        #    dy = target_j - cur_j
        #    if dx < 0:
        #        path += 'U' * (-dx)
        #    if dy < 0:
        #        path += 'L' * (-dy)
        #    if dx > 0:
        #        path += 'D' * dx
        #    if dy > 0:
        #        path += 'R' * dy
        #    path += '!'
        #    cur_i = target_i
        #    cur_j = target_j
        #return path

if __name__ == "__main__":
    soultion = Solution()
    target = 'zb'
    res = soultion.alphabetBoardPath(target)
    print(res)
    target = 'zdz'
    res = soultion.alphabetBoardPath(target)
    print(res)
