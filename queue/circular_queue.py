# -*- coding: utf-8 -*-
"""
__author__ = 'Alex wu'
__version__ = '1.0'

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。
"""


class MyCircularQueue(object):
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.__item = [None for _ in range(k+1)]
        self.maxsize = k  # 这步很关键
        self.front = -1 # 队头元素
        self.rear = -1   # 队尾元素

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.maxsize
        self.__item[self.rear] = value
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
            return True
        self.front = (self.front + 1) % self.maxsize
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.__item[self.front]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.__item[self.rear]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        # flag = True
        # for _ in self.__item:
        #     if _ is not None:
        #         flag = False
        # return flag
        return self.front == -1

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        # flag = True
        # for _ in self.__item:
        #     if not _:
        #         flag = False
        # return flag
        return (self.rear + 1) % self.maxsize == self.front




# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
param_2 = obj.enQueue(2)
param_3 = obj.enQueue(1)
param_4 = obj.enQueue(1)
print obj.isFull()
# print param_1
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()