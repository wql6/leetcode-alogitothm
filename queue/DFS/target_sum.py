# -*- coding: utf-8 -*-
"""
__author__ = 'Alex wu'
__version__ = '1.0'

给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
"""


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        setp = 0
        visited = []
        ways = 0
        target = 0
        for n in nums:
            if target == S:
                ways += 1
                continue
            target += n

    def DFS(self,nums, S,target,n,visited):
        if target == S:
            n += 1
            return n
        num = nums.pop(0)
        for n in [-num,num]:
            if n  not in visited:
                visited.append(n)
                return self.DFS(nums, S,target,n,visited)
