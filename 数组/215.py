# -*- coding: UTF-8 -*-
'''
@Project ：leetcode- 
@File    ：215.py
@IDE     ：PyCharm 
@Author  ：linsongrong
@Date    ：2021/8/10 10:45 
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.topk_spilt(nums, len(nums)-k, 0, len(nums)-1)
        return nums[len(nums)-k]


    def partition(self, nums, left, right):
        pivot = nums[left] #初始化基准
        l, r = left, right
        while l < r:
            while(l < r and nums[r] >= pivot):#从后往前查找，直到找到一个比pivot更小的数
                r -= 1
            nums[l] = nums[r] #将更小的数放入左边
            while(l < r and nums[l] <= pivot):
                l += 1
            nums[r] = nums[l]
        nums[l] = pivot
        return l

    def quicksort(self, nums, left, right):
        if left < right:
            index = self.parttition(nums, left, right)
            self.quicksort(nums, left, index - 1)
            self.quicksort(nums, index + 1, right)
        return nums

    def topk_split(self, nums, k, left, right):
        """
        将快速排序改成快速选择，即我们希望寻找到一个位置，
        这个位置左边是k个比这个位置上的数更小的数，右边是n-k个比该位置上的数大的数
        :param nums:
        :param k:
        :param left:
        :param right:
        :return:
        """
        if (left < right):
            index = self.partition(nums, left, right)
            if index == k:
                return
            elif index < k:
                self.topk_split(nums, k, index + 1, right)
            else:
                self.topk_split(nums, k, left, index - 1)


def quick_sort(list):
    less = []
    pivotList = []
    more = []
    # 递归出口
    if len(list) <= 1:
        return list
    else:
        # 将第一个值做为基准
        pivot = list[0]
        for i in list:
            # 将比急转小的值放到less数列
            if i < pivot:
                less.append(i)
            # 将比基准打的值放到more数列
            elif i > pivot:
                more.append(i)
            # 将和基准相同的值保存在基准数列
            else:
                pivotList.append(i)
        # 对less数列和more数列继续进行排序
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more

if __name__ == '__main__':
    arr = [1,5,8,1,36,7]
    print(quick_sort(arr))
