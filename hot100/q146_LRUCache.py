#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/07 21:43:54
# Author  : AI-NLP-WangXiaohui
# File    : q146_LRUCache.py
"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
 

提示：

1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put
"""
"""
思路：用字典存，保证 o(1)读取，用双向链表控制元素的时间，头节点是最近刚使用的，末尾节点是最久未使用的
     增加几个内部函数，增加头节点，删除尾节点，删除节点，移动节点为头节点
"""

class DlinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {}
        self.capacity = capacity
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        node = self.map[key]
        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.map:
            newhead = DlinkedNode(key,value)
            self.map[key] = newhead
            self.addToHead(newhead)
            if len(self.map) > self.capacity:
                remove_node = self.removeTail()
                del self.map[remove_node.key]
        else:
            node = self.map[key]
            node.value = value
            self.moveToHead(node)
    def addToHead(self, newhead):
        newhead.next = self.head.next
        self.head.next.prev = newhead
        self.head.next = newhead
        newhead.prev = self.head
    def moveToHead(self, newhead):
        self.removeNode(newhead)
        self.addToHead(newhead)
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node