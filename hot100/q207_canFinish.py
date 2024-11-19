#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/19 08:54:53
# Author  : AI-NLP-WangXiaohui
# File    :  q207_canFinish.py
'''
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

 

示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
'''
'''
思路： 1、将课程的依赖关系存储到字典中。
      2、创建一个列表，存储所有依赖数为0的课程。
      3、当列表不为空时，继续循环。
      4、遍历列表中的课程，将课程标记为已处理。
      5、如果课程有依赖关系，将依赖关系的依赖数减1。
      6、将所有依赖数为0的课程添加到列表中。
      7、统计依赖数为0的课程数量。
      8、如果依赖数为0的课程数量等于numCourses，说明可以完成所有课程，返回True。
      9、否则，返回False。
'''
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 去掉所有带环的，统计数目看是否够
        all = [0] * numCourses
        s = {}
        for (a, b) in prerequisites:
            if b not in s:
                s[b] = []
            s[b].append(a)
            all[a] += 1
        tmp = [i for i in range(len(all)) if all[i] == 0]
        # 用来判断是否遍历过，这里可以用栈优化
        s1 = {}
        while tmp != []:
            tmp1 = []
            for key in tmp:
                if key not in s1:
                    s1[key] = 1
                    if key in s:
                        for item in s[key]:
                            all[item] -= 1
                    tmp1 = [i for i in range(len(all)) if all[i] == 0]
    
            tmp = tmp1
        num = 0
        for key in all:
            if key == 0:
                num += 1
        if num == numCourses:
            return True
        else:
            return False
if __name__ == "__main__":
    s = Solution()
    numCourse = 20
    prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
    print(s.canFinish(numCourse,prerequisites))
    numCourse = 2
    prerequisites = [[1,0]]
    print(s.canFinish(numCourse,prerequisites))
    numCourse = 3
    prerequisites =[[1,0],[1,2],[0,1]]
    print(s.canFinish(numCourse,prerequisites))