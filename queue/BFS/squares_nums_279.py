# -*- coding: utf-8 -*-
"""
__author__ = 'Alex wu'
__version__ = '1.0'

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
"""


class Solution(object):
    """
     解题思路： 例如13 ，寻找首节点数为(12, 1) 步数为1 ，再将 13 - 2**2 = 9 ,(9,1) ,(4,1) 依次进队列，
     将(12,1)出队，寻找步数为2 的节点数为 (11,2) ,(8,2),(3,2) 依次进队，
     (9,1)出队，寻找节点为（8,2） ，发现已经被访问过了，跳过找到（5,2）进队
     当tNum 刚好为0 时，符合条件退出即可
    """
    def numSquares(self, n):
        vistited = [False for _ in range(n + 1)]  # 记录已被访问过的位置，如上提到的(8,2)节点
        q = []
        q.append([n, 0])
        vistited[n] = True
        while q:
            num, step = q.pop(0)
            i = 1
            tNum = num - i**2
            while tNum >= 0:
                if tNum == 0:
                    print q
                    return step + 1
                if not vistited[tNum]:
                    q.append([tNum, step + 1])
                    vistited[tNum] = True
                i += 1
                tNum = num - i**2

s = Solution()

print s.numSquares(2)

