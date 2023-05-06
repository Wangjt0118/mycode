"""
在一个长度为 n 的数组里的所有数字都在 0 到 n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字是重复的，
也不知道每个数字重复几次。请找出数组中任意一个重复的数字
要求时间复杂度 O(N)，空间复杂度 O(1)
"""
import time

nums = [3, 1, 5, 2, 0, 6, 4, 7, 4, 2]
# 交换过程
# nums = [2, 1, 5, 3, 0, 6, 4, 7, 2]
# nums = [5, 1, 2, 3, 0, 6, 4, 7, 2]
# nums = [6, 1, 2, 3, 0, 5, 4, 7, 2]
# nums = [4, 1, 2, 3, 0, 5, 6, 7, 2]
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 2]


def find_num(nums):
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[nums[i]] == nums[i]:
                return nums[i]
            t_reverse(nums, i, nums[i])
            print(nums)
    return -1


def t_reverse(nums, i, i_num):
    """
    nums: 原数组
    i: 当前循环值的下标
    i_num: 对应i下标的值
    """
    temp = nums[i]
    nums[i] = nums[i_num]
    nums[i_num] = temp


print(find_num(nums))

"""
题解：在循环过程中，把当前数字，放在列表对应下标位置上，如果当前数字和对应下标上的值相等时，则是重复
"""


